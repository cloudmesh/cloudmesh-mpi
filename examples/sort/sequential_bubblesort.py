from verify import verify
from generate import generate_random
from generate import generate_shuffle
#bubble sort
#https://www.geeksforgeeks.org/python-program-for-bubble-sort/

def bubble_sort(order, arr):
    n = len(arr)
    if order in ["ascending","<"]: 
        for i in range(n - 1):
            for j in range(n - i - 1):
                #swap unordered pairs
                if arr[j] > arr[j + 1]:
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
    elif order == "descending":
        for i in range(n - 1):
            for j in range(n - i - 1):
                #swap unordered pairs
                if arr[j] < arr[j + 1]:
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])

if __name__ == "__main__":
    #test and input
    a = []
    n = int(input())
    for i in range(n):
        x = int(input())
        a.append(x)
    bubble_sort("ascending", a)
    print(a)
    print(verify("ascending", a))
    bubble_sort("descending", a)
    print(verify("descending", a))

    bubble_sort("<", a)
    print(a)
    #assert verify("descending", a)

    a = generate_random(100)
    bubble_sort("<", a)
    print(a)
    assert verify("ascending", a)

    a = generate_shuffle("ascending", 10, 1)
    print(a)
