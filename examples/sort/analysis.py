#!/usr/bin/env python

"""
Example:
	./analysis.py --size="[100]"; gopen images/*.pdf
		create all images for the experiment with size 100

	./analysis.py --info=True
		shows the experiment ranges for count, sizes, processes

"""

from pprint import pprint

import click
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from cloudmesh.common.Shell import Shell
from cloudmesh.common.parameter import Parameter


def get_data(content, tag="multiprocessing_mergesort", size=None):
    """
    TBD

    :param content:
    :type content:
    :param name:
    :type name:
    :return:
    :rtype:
    """
    found = []
    lines = [line for line in content if "# csv" in line]

    for line in lines[1:]:
        entries = line.split(",")
        entry = [entries[a] for a in [1, 3, 9]]
        time = entry[1]
        name = entry[2]
        processes, size, count = entry[0].split(tag)[1].split("_")[1:]

        entry = [
            int(processes),
            # int(count),
            float(time),
            int(size),
            name,
            tag
        ]
        found.append(entry)
    return found

def read_log(log, size=None, tag="multiprocessing_mergesort"):
    if ".log" not in log:
        log = f"log/{log}-{size}.log"
    f = open(log, "r")
    content = f.read().splitlines()
    data = get_data(content, tag=tag, size=size)
    return data

def read_logs(files=["alex", "gregor"], size =[100], tags=["multiprocessing_mergesort"]):
    data = []
    for tag in tags:
        for file in files:
            for s in size:
                content = read_log(file, size=s, tag="multiprocessing_mergesort")
                data = data + content

    return data



# NOT USED in notebook
def generate_average(df, tag, size):
    pass



# NOT USED in notebook
def avg_simple_processes_time_fixed_size(data1, size, name=None, processes=None, label=None):
    """
    creates image from averaged data with processes and time while keeping size constant

    :param data1:
    :type data1:
    :param size:
    :type size:
    :param name:
    :type name:
    :param processes:
    :type processes:
    :param label:
    :type label:
    :return:
    :rtype:
    """

    x = []
    y = []

    for entry in data1:
        p, s, count, t = entry
        if processes is None or p in processes and s == size:
            x.append(p)
            y.append(t)
    return x, y

# NOT USED in notebook
def format_plot():
    sns.set_theme(style="darkgrid")
    df1 = pd.DataFrame({'processes': x1, 'time': y1})
    avg1 = df1.groupby(['processes']).mean()
    sns.lineplot(x="processes", y="time", data=avg1)
    plt.show()

# NOT USED in notebook
def get_ranges(data):
    """
    TBD

    :param data:
    :type data:
    :return:
    :rtype:
    """
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

# NOT USED in notebook
def processes_time_fixed_size(data, size, name=None, processes=None, label=None):
    """
    creates image from data with processes and time while keeping size constant

    :param data:
    :type data:
    :param size:
    :type size:
    :param name:
    :type name:
    :param processes:
    :type processes:
    :param label:
    :type label:
    :return:
    :rtype:
    """
    x = []
    y = []
    result = []

    for entry in data:
        label, p, s, count, t, total, host, user = entry
        if processes is None or p in processes and s == size:
            x.append(p)
            y.append(t)

    result = {
        "x": x,
        "y": y
    }

    pprint(x)
    pprint(y)

    if name == None:
        name = f"images/processes_time_{size}"
    sns.set_theme(style="ticks", palette="pastel")
    ax = sns.boxplot(x="x", y="y", data=result)
    label = label.replace("_", " ")
    ax.set_title(f"{label}, size={size}")
    ax.set_ylabel("Time/s")
    ax.set_xlabel("Processes")
    # plt.savefig(f"{name}.png")
    # plt.savefig(f"{name}.pdf")
    plt.show()
    plt.close()

# NOT USED in notebook
def avg_processes_time_fixed_size(data1, size, name=None, processes=None, label=None):
    """
    creates image from averaged data with processes and time while keeping size constant

    :param data1:
    :type data1:
    :param size:
    :type size:
    :param name:
    :type name:
    :param processes:
    :type processes:
    :param label:
    :type label:
    :return:
    :rtype:
    """

    x1 = []
    y1 = []

    for entry in data1:
        label, p, s, count, t, total, host, user = entry
        if processes is None or p in processes and s == size:
            x1.append(p)
            y1.append(t)

    sns.set_theme(style="darkgrid")
    df1 = pd.DataFrame({'processes': x1, 'time': y1})
    avg1 = df1.groupby(['processes']).mean()
    ax = sns.lineplot(x="processes", y="time", data=avg1)
    ax.set_title(f"{label}, size={size}")
    ax.set_ylabel("Time/s")
    ax.set_xlabel("Processes")
    plt.show()

# NOT USED in notebook
def speedup_fixed_size(data, size, name, processes):
    """
    creates image from data to show speedup with fixed size

    :param data:
    :type data:
    :param size:
    :type size:
    :param name:
    :type name:
    :param processes:
    :type processes:
    :return:
    :rtype:
    """
    x = []
    y = []
    result = []
    nums = []
    pprint(processes)
    for p in processes:
        print(p)
        temp = []
        for entry in data:
            label, p, s, count, t, total, host, user = entry
            if size == s:
                print("HERE")
                print(t)
                temp.append(t)
        nums.append(temp)
    pprint(nums)
    time_0 = sum(nums[0][i] for i in len(nums[0])) / len(nums[0])
    for i in len(nums):
        time = sum(nums[i][j] for j in len(nums[i])) / len(nums[i])
        x.append(processes[i])
        y.append(float(time_0 / time))
        result.append([processes[i], float(time_0 / time)])

    if name == None:
        name = f"speedup_{size}"
    sns.set_theme(style="ticks", palette="pastel")
    ax = sns.boxplot(x="x", y="y", data=result)
    label = label.replace("_", " ")
    ax.set_title(f"{label}, size={size}")
    ax.set_ylabel("speedup")
    ax.set_xlabel("processes")
    # plt.savefig(f"{name}.png")
    # plt.savefig(f"{name}.pdf")
    plt.show()
    plt.close()


# plt.savefig('images/size.pdf')

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
    """
    performance experiment.

    :param processes:
    :type processes:
    :param size:
    :type size:
    :param repeat:
    :type repeat:
    :param log:
    :type log:
    :param debug:
    :type debug:
    :param sort:
    :type sort:
    :param x:
    :type x:
    :param y:
    :type y:
    :param info:
    :type info:
    :return:
    :rtype:
    """

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

    f = open(log, "r")
    content = f.read().splitlines()
    data = get_data(content, name=sort)
    for size in sizes:
        avg_processes_time_fixed_size(data, size, label=sort)
    if debug:
        print(content)
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
