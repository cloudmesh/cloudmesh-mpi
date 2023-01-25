# merge sort
# https://www.educative.io/edpresso/merge-sort-in-python

def merge_sort(order, arr):
    if order in ["ascending", "<"]:
        return merge_sort_smaller(arr)
    elif order in ["descending", ">"]:
        return merge_sort_bigger(arr)

def merge_sort_smaller(array):
    if len(array) > 1:

        r = len(array) // 2
        left = array[:r]
        right = array[r:]

        merge_sort_smaller(left)
        merge_sort_smaller(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array

def merge_sort_bigger(array):
    if len(array) > 1:

        r = len(array) // 2
        left = array[:r]
        right = array[r:]

        merge_sort_bigger(left)
        merge_sort_bigger(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array
