def get_depth(n,testsets):
    depth = {}
    # code to calculate depth of each vertex
    for i in range(n):
        depth[i] = 0
    for i in testsets:
        depth[i[0]] += 1
    return depth   

def get_seq(n,testsets):
    # code to detect deadlock
    print(testsets)
    sets = [set(i) for i in testsets]
    list1 = []
    for i in sets:
        if i not in list1:
            list1.append(i)
    if len(list1) != len(sets):
        return("deadlock detected")
    
    depth = get_depth(n,testsets)
    answer = [x for x in depth.keys() if depth[x] == 0]
    while  len(testsets) > 0:
        for i in testsets:
            if i[1] in answer:
                testsets.remove(i)
        depth = get_depth(n,testsets)
        temp = [x for x in depth.keys() if depth[x] == 0]
        for a in temp:
            if a not in answer:
                answer.append(a)
    return answer

# kahn's algorithm for topological sort        
# Here 2 is dependend on 1, 3 depends on 2, 5 depends on 1 and so on        
print(get_seq(10,[(1,2),(2,3),(1,5),(2,3),(7,6),(9,2),(8,0)]))
# here 2 depends on 3, 3 depends on 1, 4 depends on 0, 4 also depends on 1 and so on
print(get_seq(6,[(2,3),(3,2),(1,3),(0,4),(1,4),(0,5),(2,5)]))
