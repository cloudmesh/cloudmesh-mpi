from generate import generate_random
from cloudmesh.common.StopWatch import StopWatch
from verify import verify

def assess(sort_type, sort_name):
    for n in [10, 100, 1000]:
            a = generate_random(n)
            StopWatch.start(f"{sort_name}_{n}")
            sort_type("<", a)
            StopWatch.stop(f"{sort_name}_{n}")
            assert verify("ascending", a)
    StopWatch.benchmark()