# bubble sort
# https://www.geeksforgeeks.org/python-program-for-bubble-sort/

def bubblesort(order, arr):
    n = len(arr)
    if order in ["ascending", "<"]:
        for i in range(n - 1):
            for j in range(n - i - 1):
                # swap unordered pairs
                if arr[j] > arr[j + 1]:
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
    elif order in ["descending", ">"]:
        for i in range(n - 1):
            for j in range(n - i - 1):
                # swap unordered pairs
                if arr[j] < arr[j + 1]:
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])


