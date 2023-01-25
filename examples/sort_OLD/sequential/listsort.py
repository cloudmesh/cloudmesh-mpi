def listsort(order, arr):
    if order in ["ascending", "<"]:
        return arr.sort()
    elif order in ["descending", ">"]:
        return arr.sort(reverse=True)

def listsorted(order, arr):
    # less efficient than slistsort
    if order in ["ascending", "<"]:
        return sorted(arr)
    elif order in ["descending", ">"]:
        return sorted(arr, reverse=True)
