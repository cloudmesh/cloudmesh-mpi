from generate import generate_random
from cloudmesh.common.StopWatch import StopWatch
from verify import verify

debug = False

def assess(sort_type, sort_name):
	for n in [10, 100, 1000]:
		a = generate_random(n)
		if debug:
			print(a)
		StopWatch.start(f"{sort_name}_{n}_1")
		sort_type("<", a)
		StopWatch.stop(f"{sort_name}_{n}_1")
		if debug:
			print(a)
		assert verify("ascending", a)
	StopWatch.benchmark()

def multiprocessing_benchmark(sort_type, sort_name, processes, size):
	a = generate_random(size)
	if debug: 
		print(a)
	StopWatch.start(f"{sort_name}_{size}_{processes}")
	a = sort_type(a, processes) 
	StopWatch.stop(f"{sort_name}_{size}_{processes}")
	if debug:
		print(a)
	assert verify("ascending", a)
	StopWatch.benchmark()