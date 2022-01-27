#!/usr/bin/env python
from generate import generate_random
from cloudmesh.common.StopWatch import StopWatch
from verify import verify
import click
from cloudmesh.common.util import yn_choice
from cloudmesh.common.parameter import Parameter

def get_sort_by_name(name="multiprocessing_mergesort"):
	if name in ["mp-mergesort", "multiprocessing_mergesort"]:
		from multiprocessing_mergesort import multiprocessing_mergesort
		return multiprocessing_mergesort
	else:
		return None

def get_label(name, p, n, i, tag=None):
	if tag is None:
		tag = os.uname().nodename
	return f"{tag}_{sort}_{p}_{n}_{i}"


@click.command()
@click.option('--processes', default="[1]", help='Number of processes as array. [1-2,8,16]')
@click.option('--size', default="[100]", help='Total size of the array to be sorted as array. [10, 100]')
@click.option('--repeat', default=1, help='number of times an experiment with processes and size is repeated. 1')
@click.option('--log', default="output.log", help='The logfile to which the '
												  'experiments are appended')
@click.option('--clear', default=False, help='Clears the logfile. Handle with care')
@click.option('--debug', default=False, help='Switch on some debugging')
@click.option('--sort', default="multiprocessing_mergesort", help="sorting function")
def experiment(processes, size, repeat, log, clear, debug, sort):
	"""performance experiment."""

	if clear:
		c = yn_choice("Would you like to clear the file {log} before running the experiements")
		if not c:
			return ""

	processes = Parameter.expand(processes)
	sizes = Parameter.expand(size)

	processes = [int(number) for number in processes]
	sizes = [int(number) for number in sizes]

	print("Starting experiment")


	print(f"Log:       {log}")
	print(f"Processes: {processes}")
	print(f"Size:      {sizes}")
	print(f"Repeat:    {repeat}")
	print(f"Clear:     {clear}")
	print(f"Debug:     {debug}")
	print(f"Algorithm: {sort}")

	sort_algorithm = get_sort_by_name(sort)
	for p in processes:
		for n in sizes:
			for i in range(repeat):
				print(f"Experiment: size={n} processes={p} repeat={i}")
				label = get_label(sort, p, n, i)
				a = generate_random(n)
				if debug:
					print(a)
				StopWatch.start(label)
				a = sort_algorithm(a, p)
				StopWatch.stop(label)
				if debug:
					print(a)
				assert verify("ascending", a)
	StopWatch.benchmark()

if __name__ == '__main__':
	log, processes, sizes, repeat, clear, debug= experiment()
