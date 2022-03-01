from cloudmesh.common.StopWatch import StopWatch
from generate import Generator


# bubble sort
# https://www.geeksforgeeks.org/python-program-for-bubble-sort/

def bubble_sort(order, arr):
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


if __name__ == "__main__":
    n = 100
    a = Generator.random(n)
    StopWatch.start(f"bubble_sort {n}")
    bubble_sort("<", a)
    StopWatch.stop(f"bubble_sort {n}")
    print(a)
    StopWatch.benchmark()
