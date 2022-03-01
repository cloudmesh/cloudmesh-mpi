from sequential.bubblesort import bubblesort
from sequential.heapsort import heapsort
from sequential.quicksort import quicksort
from sequential.insertionsort import insertionsort
from sequential.selectionsort import selectionsort
from sequential.listsort import listsort

#from sequential_numba.bubblesort import bubblesort as bubblesort_numba
#from sequential_numba.heapsort import heapsort as heapsort_numba
#from sequential_numba.quicksort import quicksort as quicksort_numba
from sequential_numba.insertionsort import insertionsort as insertionsort_numba
#from sequential_numba.selectionsort import selectionsort as selectionsort_numba

from cloudmesh.common.StopWatch import StopWatch
from generate import Generator

StopWatch.benchmark(sysinfo=True, user="gregor", node="5950x")



for n in [100,1000,10000]:
    numbers = Generator.random(n)

    for sort in [
        listsort,
        selectionsort,
        quicksort,
        insertionsort,
        heapsort,
        bubblesort,
        #selectionsort_numba,
        #quicksort_numba,
        #insertionsort_numba,
        #heapsort_numba,
        #bubblesort_numba

    ]:

        name = str(sort.__name__)
        print(f"{name:>20} {n:>10} ", end="")
        a = numbers.copy()
        StopWatch.start(f"{name} {n}")
        sort("<", a)
        StopWatch.stop(f"{name} {n}")
        assert Generator.verify("<", a)
        t = StopWatch.get(f"{name} {n}")
        print(f"{t:<6}")

StopWatch.benchmark(sysinfo=False, user="gregor", node="5950x")
