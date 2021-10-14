#a = [2,8,15,18,20,30,40]
#b = [5,9,12,17,50,60,70,80,90]
#c = []

def merge(a,b):
    m = len(a)
    n = len(b)
    i,j= 0,0
    while(i < m and j < n):  
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c


#print(merge(a,b))


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        mergesort(L)
        R = arr[mid:]
        mergesort(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
        


arr = list(range(99999999))
print("done")
import random
random.shuffle(arr)
print("done")
mergesort(arr)
print("done")

