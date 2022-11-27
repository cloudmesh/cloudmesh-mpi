import sequential


class Sort:

    def __init__(self, kind=None, parallel=None, mode=None, n=None):
        self.kind = kind
        self.mode = mode
        self.parallel = parallel
        self.a = None
        self.n = n

    def random_array(self, seed=None):
        """
        Generates a random array with the given seed if specified.
        """
        if self.parallel == "sequential":
            raise NotImplementedError

    def get(self):
        """
        returns the array
        """

    def verify(self):
        raise NotImplementedError

    def sort(self, order="<"):

        if self.parallel == "sequential" and self.mode == "numba":
            if self.kind == "quicksort":
                algorithm = sequential.numba.quicksort
            elif self.kind == "bubblesort":
                algorithm = sequential.numba.bubblesort
            elif self.kind == "heapsort":
                algorithm = sequential.numba.heapsort
            elif self.kind == "insertionsort":
                algorithm = sequential.numba.insertionsort
            elif self.kind == "listsort":
                algorithm = sequential.numba.listsort
            elif self.kind == "mergesort":
                algorithm = sequential.numba.mergesort
            elif self.kind == "selectionsort":
                algorithm = sequential.numba.selectionsort

        elif self.parallel == "sequential":
            if self.kind == "quicksort":
                algorithm = sequential.quicksort
            elif self.kind == "bubblesort":
                algorithm = sequential.bubblesort
            elif self.kind == "heapsort":
                algorithm = sequential.heapsort
            elif self.kind == "insertionsort":
                algorithm = sequential.insertionsort
            elif self.kind == "listsort":
                algorithm = sequential.listsort
            elif self.kind == "mergesort":
                algorithm = sequential.mergesort
            elif self.kind == "selectionsort":
                algorithm = sequential.selectionsort

        else:

            raise NotImplementedError

        algorithm(order, self.a)
