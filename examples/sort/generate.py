import random


class Generator:

    @staticmethod
    def input():
        a = []
        n = int(input())
        for i in range(n):
            x = int(input())
            a.append(x)
        return a

    @staticmethod
    def random(n):
        a = []
        for i in range(n):
            x = random.randint(0, n)
            a.append(x)
        return a

    @staticmethod
    def shuffle(order, n, m):
        if order in ["ascending", "<"]:
            a = []
            for i in range(n):
                a.append(i)
            for i in range(m):
                x1 = random.randint(0, n)
                x2 = random.randint(0, n)
                a[x1], a[x2] = a[x2], a[x1]
            return a
        elif order in ["descending", ">"]:
            a = []
            for i in range(n, 0):
                a.append(i)
            for i in range(m):
                x1 = random.randint(0, n)
                x2 = random.randint(0, n)
                a[x1], a[x2] = a[x2], a[x1]
            return a

    @staticmethod
    def verify(order, a):
        n = len(a)
        if order in ["<", "ascending"]:
            for i in range(n - 1):
                if a[i] > a[i + 1]:
                    return False
            return True
        elif order in [">", "descending"]:
            for i in range(n - 1):
                if a[i] < a[i + 1]:
                    return False
            return True
