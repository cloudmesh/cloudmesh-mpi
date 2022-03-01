from sequential.bubblesort import bubblesort
from sequential.heapsort import heapsort
from sequential.quicksort import quicksort
from sequential.insertionsort import insertionsort
from sequential.selectionsort import selectionsort

from cloudmesh.common.StopWatch import StopWatch
from generate import Generator

StopWatch.benchmark(sysinfo=True, user="gregor", node="5950x")



for n in [100,1000,10000]:
    numbers = Generator.random(n)

    for sort in [
        selectionsort,
        quicksort,
        insertionsort,
        heapsort,
        bubblesort
        ]:

        name = str(sort.__name__)
        print(name)
        a = numbers.copy()
        StopWatch.start(f"{name} {n}")
        sort("<", a)
        StopWatch.stop(f"{name} {n}")
        assert Generator.verify("<", a)

StopWatch.benchmark(sysinfo=False, user="gregor", node="5950x")
