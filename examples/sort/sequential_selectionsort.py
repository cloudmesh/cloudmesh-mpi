# selection sort


def selection_sort(arr, n):
    for i in range(n):
        # find min element in unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # place min element at end of sorted array
        (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])


if __name__ == "__main__":
    # input and testing
    a = []
    n = int(input())
    for i in range(n):
        x = int(input())
        a.append(x)
    selection_sort(a, len(a))
    print(a)
