from verify import verify
from generate import generate_random
from generate import generate_shuffle
from cloudmesh.common.StopWatch import StopWatch
from performance import assess
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
    elif order in ["descending",">"]: 
        for i in range(n - 1):
            for j in range(n - i - 1):
                #swap unordered pairs
                if arr[j] < arr[j + 1]:
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])

if __name__ == "__main__":
    #test and input
    a = []
    #assert verify("descending", a)
    assess(bubble_sort, "bubble_sort")

    a = generate_shuffle("ascending", 10, 1)
    print(a)
    StopWatch.benchmark()
