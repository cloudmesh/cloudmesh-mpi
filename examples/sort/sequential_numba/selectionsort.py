from numba import jit


@jit
def selectionsort(order, arr):
    n = len(arr)

    if order in ["<"]:
        for i in range(n):
            # find min element in unsorted array
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            # place min element at end of sorted array
            (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])
    else:
        for i in range(n):
            # find min element in unsorted array
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] > arr[min_idx]:
                    min_idx = j
            # place min element at end of sorted array
            (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])
