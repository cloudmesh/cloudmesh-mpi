from generate import Generator
from cloudmesh.common.StopWatch import StopWatch


# quicksort
# https://www.geeksforgeeks.org/python-program-for-quicksort/


# partition array into two sections
def split(arr, l, r):
    i = l + 1
    j = r
    k = arr[l]  # partition variable

    while True:
        # find j to the right of k and less than k
        while i <= j and arr[j] >= k:
            j -= 1
        # find i to the left of k and greater than k
        while i <= j and arr[i] <= k:
            i += 1
        # swap so both are in correct location
        if (i <= j):
            (arr[i], arr[j]) = (arr[j], arr[i])
        else:
            break
    # arr[l] = k, must be put into proper position
    (arr[l], arr[j]) = (arr[j], arr[l])
    return j


def quicksort(arr, l=None, r=None):
    if l is None:
        l = 0
    if r is None:
        r = len(a) - 1
    if l >= r:
        return
    k = split(arr, l, r)
    # don't include k, since it's already sorted
    quicksort(arr, l, k - 1)
    quicksort(arr, k + 1, r)


if __name__ == "__main__":
    n = 100
    a = Generator.random(n)
    StopWatch.start(f"bubble_sort {n}")
    quicksort("<", a)
    StopWatch.stop(f"bubble_sort {n}")
    print(a)
    StopWatch.benchmark()
