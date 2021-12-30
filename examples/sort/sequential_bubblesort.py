#bubble sort
#https://www.geeksforgeeks.org/python-program-for-bubble-sort/

def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            #swap unordered pairs
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])

#test and input
a = []
n = int(input())
for i in range(n):
    x = int(input())
    a.append(x)
bubble_sort(a, len(a))
print(a)
