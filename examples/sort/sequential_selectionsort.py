from generate import Generator
from cloudmesh.common.StopWatch import StopWatch

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # find min element in unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # place min element at end of sorted array
        (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])

if __name__ == "__main__":
    n = 100
    a = Generator.random(n)
    StopWatch.start(f"bubble_sort {n}")
    selection_sort("<", a)
    StopWatch.stop(f"bubble_sort {n}")
    print(a)
    StopWatch.benchmark()
