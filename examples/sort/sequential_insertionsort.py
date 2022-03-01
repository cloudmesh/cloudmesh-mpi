from cloudmesh.common.StopWatch import StopWatch

from generate import Generator

# insertion sort

def insertion_sort(order, arr):
    n = len(arr)
    if order in ["ascending", "<"]:
        for i in range(1, n):
            x = arr[i]
            j = i - 1
            # shift all elements greater than x to the right by 1
            while j >= 0 and x < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            # insert x
            arr[j + 1] = x
    elif order in ["descending", ">"]:
        for i in range(1, n):
            x = arr[i]
            j = i - 1
            # shift all elements less than x to the right by 1
            while j >= 0 and x > arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            # insert x
            arr[j + 1] = x


# test and input
if __name__ == "__main__":
    n = 100
    a = Generator.random(n)
    StopWatch.start(f"insertion_sort {n}")
    insertion_sort("<", a)
    StopWatch.stop(f"insertion_sort {n}")
    print(a)
    StopWatch.benchmark()
