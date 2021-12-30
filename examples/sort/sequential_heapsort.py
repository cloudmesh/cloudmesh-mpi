#heap sort

#using binary tree
#left child of node i = 2i + 1
#right child of node i = 2i + 2
#parent of node i = (i - 1) / 2

import sys;

def heapify(arr, n, i):
    big = i
    #node i's two children
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[big]:
        big = l
    if r < n and arr[r] > arr[big]:
        big = r

    #if l or r greater than i, swap
    if big != i:
        (arr[i], arr[big]) = (arr[big], arr[i])
        #heapify again on new i
        heapify(arr, n, big)

def heapsort(arr, n):
    #build max heap from bottom up
    for i in range(n / 2, -1, -1):
          heapify(arr, n, i)

    #swap and heapify
    for i in range(n - 1, 0, -1):
        #swap max of current heap to position i and remove from heap
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        heapify(arr, i, 0)
        
if __name__ == "__main__":
    a = []
    n = int(input())
    for i in range(n):
        x = int(input())
        a.append(x)
    heapsort(a, n)
    print(a)

