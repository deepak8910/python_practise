def dup(a):
    temp = []
    for i in a:
        if i not in temp:
            temp.append(i)
    return temp


a = [1,2,4,2,3,6,4,3,6,8,0,4,2,0]
print(a,"\n",dup(a))