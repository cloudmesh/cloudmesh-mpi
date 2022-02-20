def verify(order, a):
    n = len(a)
    if order == "ascending":
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                return False
        return True
    elif order == "descending":
        for i in range(n - 1):
            if a[i] < a[i + 1]:
                return False
        return True
