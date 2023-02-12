# merge sort
# https://www.educative.io/edpresso/merge-sort-in-python

from util.generate import Generator

def mergesort(order, arr):
    if order in ["ascending", "<"]:
        return mergesort_smaller(arr)
    elif order in ["descending", ">"]:
        return mergesort_bigger(arr)

def mergesort_smaller(array):
    if len(array) > 1 and not Generator.verify('<', array):

        r = len(array) // 2
        left = array[:r]
        right = array[r:]

        mergesort_smaller(left)
        mergesort_smaller(right)

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
    print(array)
    return array

def mergesort_bigger(array):
    if len(array) > 1 and not Generator.verify('>', array):

        r = len(array) // 2
        left = array[:r]
        right = array[r:]

        mergesort_bigger(left)
        mergesort_bigger(right)

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
    print(array)
    return array
