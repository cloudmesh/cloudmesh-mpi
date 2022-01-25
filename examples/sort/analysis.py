#!/usr/bin/env python

"""
Example:
	./analysis.py --size="[100]"; gopen images/*.pdf
		create all images for the experiment with size 100
		
	./analysis.py --info=True
		shows the experiment ranges for count, sizes, processes

"""

import click
from cloudmesh.common.util import yn_choice
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import readfile
from cloudmesh.common.Shell import Shell
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint

def get_data(content, name="multiprocessing_mergesort"):
	found = []
	"csv,multiprocessing_mergesort_1_10000_3,ok,0.305,2.24,2022-01-23 22:40:24,,None,BL-UITS-NWLT005,alexandra,Darwin,10.15.7 "
	lines = Shell.find_lines_with(content, what=f"# csv,{name}_")
	for line in lines:
		entries = line.split(",")
		entry = [entries[a] for a in [1,3,4]]
		processes, size, count = entry[0].split(name)[1].split("_")[1:]
		entry = [name, int(processes), int(size), int(count), float(entry[1]), float(entry[2])]
		found.append(entry)
	return found

def get_ranges(data):
	processes = []
	sizes = []
	counts = []
	for line in data:
		name, p, s, c, time, total = line
		processes.append(p)
		sizes.append(s)
		counts.append(c)
	return {
		"processes": list(set(processes)),
		"sizes": list(set(sizes)),
		"counts": len(list(set(counts)))
	}

def processes_time_fixed_size(data, size, name=None, processes=None, label=None):
	"""creates image from data with processes and time while keeping size constant"""
	x = []
	y = []
	result = []
	for entry in data:
		label, p, s, count, t, total = entry
		if processes is None or p in processes and s==size:
			x.append(p)
			y.append(t)

	result = {
		"x": x,
		"y": y
	}

	if name is None:
		name = f"images/processes_time_{size}"
	sns.set_theme(style="ticks", palette="pastel")
	ax = sns.boxplot(x="x", y="y", data=result)
	label = label.replace("_", " ")
	ax.set_title(f"{label}, size={size}")
	ax.set_ylabel("time/s")
	ax.set_xlabel("processes")
	plt.savefig(f"{name}.png")
	plt.savefig(f"{name}.pdf")
	# plt.show()
	plt.close()

def speedup_fixed_size(name, data, size):
	"""creates image from data to show speedup with fixed size"""
	pass
	plt.savefig('images/size.pdf')

@click.command()
@click.option('--processes', default="[1]", help='Number of processes as array. [1-2,8,16]')
@click.option('--size', default="[100]", help='Total size of the array to be sorted as array. [10, 100]')
@click.option('--repeat', default=1, help='number of times an experiment with processes and size is repeated. 1')
@click.option('--log', default="output.log", help='The logfile to which the '
											  'experiments are appended')
@click.option('--debug', default=False, help='Switch on some debugging')
@click.option('--sort', default="multiprocessing_mergesort", help="sorting function")
@click.option('--x', help="value for x axis", default=None)
@click.option('--y', help="value for y axis", default=None)
@click.option('--info', help="value for y axis", default=False)
def analysis(processes, size, repeat, log, debug, sort, x, y, info):
	"""performance experiment."""

	processes = Parameter.expand(processes)
	sizes = Parameter.expand(size)

	processes = [int(number) for number in processes]
	sizes = [int(number) for number in sizes]

	print("Starting Analysis")
	print(f"Log:       {log}")
	print(f"Processes: {processes}")
	print(f"Size:      {sizes}")
	print(f"Repeat:    {repeat}")
	print(f"Sort:      {sort}")
	print(f"Logfile:   {log}")
	print(f"Debug:     {debug}")

	content = readfile(log).splitlines()
	data = get_data(content, name=sort)
	if debug:
		pprint(data)

	if info:
		pprint(get_ranges(data))
		return

	try:
		Shell.run("mkdir -p images")
	except:
		pass

	# BUG: this is just hardcoded and does not take the parameters, but
	# shows that we can create images from data easier
	for size in sizes:
		processes_time_fixed_size(data, size, label=sort)


if __name__ == '__main__':
	analysis()
