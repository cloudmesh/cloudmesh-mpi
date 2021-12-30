#quicksort
#https://www.geeksforgeeks.org/python-program-for-quicksort/
import sys;

#partition array into two sections
def split(arr, l, r):
    i = l + 1
    j = r
    k = arr[l] #partition variable

    while True:
        #find j to the right of k and less than k
        while i <= j and arr[j] >= k:
            j -= 1
        #find i to the left of k and greater than k
        while i <= j and arr[i] <= k:
            i += 1
        #swap so both are in correct location
        if (i <= j):
            (arr[i], arr[j]) = (arr[j], arr[i])
        else: 
            break
    #arr[l] = k, must be put into proper position
    (arr[l], arr[j]) = (arr[j], arr[l])
    return j
    
def quicksort(arr, l, r):
    if l >= r:
        return
    k = split(arr, l, r)
    #don't include k, since it's already sorted
    quicksort(arr, l, k - 1)
    quicksort(arr, k + 1, r)

a = []
n = int(input())
for i in range(n):
    x = int(input())
    a.append(x)
quicksort(a, 0, n - 1)
print(a)
