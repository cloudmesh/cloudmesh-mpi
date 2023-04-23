# merge sort
# https://www.educative.io/edpresso/merge-sort-in-python

from util.generate import Generator


# TODO: why do we need a generator?
# TODO: this has limitation that list must be dividable
#  by some number document. (e.g. power of 2). verify
# TODO: docstrings are missing

def mergesort(order, arr):
    """"
    Sorts the given array with type defined at creation time with
    a mergesort algorithm.

    :param order: the order in which to sort. It has the value "<" for
                  ascending and ">" for descending.
    :type order: str
    :param arr: The array to be sorted. This can be a numerical array
                including int or float
    :type arr: defined when the array is created.
    :return: sorted array
    :rtype: the type of the original array
    """
    if order in ["ascending", "<"]:
        return mergesort_smaller(arr)
    elif order in ["descending", ">"]:
        return mergesort_bigger(arr)

def mergesort_smaller(array):
    """

    :param array:
    :type array:
    :return:
    :rtype:
    """
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
    """

    :param array:
    :type array:
    :return:
    :rtype:
    """
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
