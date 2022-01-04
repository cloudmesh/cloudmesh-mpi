from verify import verify
from generate import generate_random
from generate import generate_shuffle
from cloudmesh.common.StopWatch import StopWatch
from performance import assess
#insertion sort

def insertion_sort(order, arr):
    n = len(arr)
    if order in ["ascending","<"]: 
        for i in range(1, n):
            x = arr[i]
            j = i - 1
            #shift all elements greater than x to the right by 1
            while j >= 0 and x < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            #insert x
            arr[j + 1] = x
    elif order in ["descending",">"]: 
        for i in range(1, n):
            x = arr[i]
            j = i - 1
            #shift all elements less than x to the right by 1
            while j >= 0 and x > arr[j]:
                arr[j + 1] = arr[j] 
                j -= 1
            #insert x
            arr[j + 1] = x


#test and input
if __name__ == "__main__":
    a = []
    a = generate_random(20)
    insertion_sort(">", a)
    print(verify("ascending", a))
    print(a)

    assess(insertion_sort, "insertion_sort")
