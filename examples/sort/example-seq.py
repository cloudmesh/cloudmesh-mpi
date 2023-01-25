from sequential.bubblesort import bubblesort as sort
from util.generate import Generator
from cloudmesh.common.StopWatch import StopWatch

n = 2000
label = f'bubblesort-{n}'

arr = Generator.generate_random(n)
StopWatch.start(label)
sort('>', arr)
StopWatch.stop(label)
print(Generator.verify('>', arr))
StopWatch.benchmark()