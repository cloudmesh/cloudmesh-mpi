#!/usr/bin/env python
from pprint import pprint

import click
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import json

from cloudmesh.common.Shell import Shell
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.dotdict import dotdict

# takes in content from logfile
# outputs dictionaries of data
def get_data(content):
    result = []
    lines = Shell.find_lines_with(content, "# csv")[1:]

    print(lines)
    for line in lines:
        line = line.replace("'", '"')
        data = "{" + line.split("{")[1].split("},")[0] + "}"
        print(data)
        data = dotdict(json.loads(data))

        line = line.split(",",6)
        t = line[3]
        data["t"] = t
        result.append(dict(data))
    return result

def read_log(log):
    if ".log" not in log:
        log = f"{log}.log"
    if "log/" not in log:
        log = f"log/{log}"
    f = open(log, "r")
    content = f.read().splitlines()
    data = get_data(content)
    return data

def read_logs(files=["alex", "gregor"], size =[100], tags=["multiprocessing_mergesort"]):
    data = []
    for tag in tags:
        for file in files:
            for s in size:
                content = read_log(file, size=s, tag="multiprocessing_mergesort")
                data = data + content

    return data

def generate_average(df, tag=None, size=None, name=None):
    _df = df.loc[(df['name'] == name) & (df['tag'] == tag) &  (df['size'] == size) ]
    avg = _df.groupby(['processors', 'name', 'size', 'tag']).mean()
    avg['tag'] = tag
    avg['name'] = name
    return avg

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
    processes data output by experiment.py from specified sort

    :param processes: processes to run multiprocessing sort on
    :type processes: int array
    :param size: sizes to run sort on 
    :type size: int array
    :param repeat: number of times an experiment with processes and size is repeated
    :type repeat: int
    :param log: logfile in which data is stored
    :type log: string
    :param debug: debugging mode
    :type debug: bool
    :param sort: type of sort to be run 
    :type sort: string
    :param x: x axis label (on graph)
    :type x: string
    :param y: y axis label (on graph)
    :type y: string
    :param info:
    :type info:
    :return: none
    :rtype: none
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
    if debug:
        print(content)
        pprint(data)

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
