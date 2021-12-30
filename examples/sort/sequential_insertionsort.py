#insertion sort
import sys;

def insertion_sort(arr, n):
    for i in range(1, n):
        x = arr[i]
        j = i - 1
        #shift all elements greater than x to the right by 1
        while j >= 0 and x < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        #insert x
        arr[j + 1] = x

#test and input
a = []
n = int(input())
for i in range(n):
    x = int(input())
    a.append(x)
insertion_sort(a, len(a))
print(a)
