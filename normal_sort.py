def linear_sort(arr):
    i = j = 0
    for i in range(i,len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


arr = list(range(99999999))
import random
random.shuffle(arr)
print("done")
linear_sort(arr)
print("done")

