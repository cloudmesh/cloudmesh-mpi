# merge sort
# https://www.educative.io/edpresso/merge-sort-in-python
from generate import Generator
from cloudmesh.common.Shell import StopWatch

def sequential_mergesort(arr):
    n = len(arr)
    if n > 1:
        # split array into left and right half
        mid = n / 2
        l = arr[:mid]
        r = arr[mid:]

        # sort left and right halves individually
        sequential_mergesort(l)
        sequential_mergesort(r)

        # i for left half, j for right half, k for arr
        i = j = k = 0
        while i < len(l) and j < len(r):
            # each time choose between element at front of l or r
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            # add to arr
            k += 1

        # add any unused elements
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


if __name__ == "__main__":
    n = 100
    a = Generator.random(n)
    StopWatch.start(f"sequential_mergesort_sort {n}")
    sequential_mergesort("<", a)
    StopWatch.stop(f"sequential_mergesort_sort {n}")
    print(a)
    StopWatch.benchmark()
