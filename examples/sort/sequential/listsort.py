def listsort(order, arr):
    if order in ["ascending", "<"]:
        return arr.sort()
    elif order in ["descending", ">"]:
        return arr.sort(reverse=True)

