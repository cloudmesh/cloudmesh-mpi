#!/usr/bin/env python
from fileinput import filename
from pprint import pprint

import click
import os
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
    lines = Shell.find_lines_with(content, "# csv")

    for line in lines:
        if "# csv,timer,status" not in line:
            line = line.replace("'", '"')
            data = "{" + line.split("{")[1].split("},")[0] + "}"
            print(data)
            data = data.replace(', "debug": False', '')
            data = dotdict(json.loads(data))

            line = line.split(",",6)
            time = line[3]
            data["time"] = time
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

def generate_df():
    directory = "log"
    all_data = []
    for file in os.listdir(directory):
        if "mpi" not in file:
            f = os.path.join(directory, file)
            all_data.extend(read_log(f))

    df = pd.DataFrame(all_data)
    df['time'] = df['time'].astype(float)
    return df

def mpi_get_data(content):
    result = []
    lines = Shell.find_lines_with(content, "# csv")
    _lines = []
    for line in lines:
        if "# csv,timer,status" not in line:
            _lines.append(line)
    
    lines = _lines
    # print(lines)
    n = len(lines)
    for i in range(0, n, 2):
        line_total = lines[i]
        line_gen = lines[i + 1]

        line_total = line_total.replace("'", '"')
        data = "{" + line_total.split("{")[1].split("},")[0] + "}"
        data = data.replace(', "debug": False', '')
        # print(data)
        data = dotdict(json.loads(data))

        line_total = line_total.split(",",6)
        time_total = line_total[3]

        line_gen = line_gen.split(",",6)
        time_gen = line_gen[3]

        data["time"] = float(time_total) - float(time_gen)
        result.append(dict(data))
    return result

def mpi_read_log(log):
    if ".log" not in log:
        log = f"{log}.log"
    if "log/" not in log:
        log = f"log/{log}"
    f = open(log, "r")
    content = f.read().splitlines()
    data = mpi_get_data(content)
    return data

def mpi_generate_df():
    directory = "log"
    all_data = []
    for file in os.listdir(directory):
        if "mpi" in file:
            # print(file)
            f = os.path.join(directory, file)
            all_data.extend(mpi_read_log(f))

    df = pd.DataFrame(all_data)
    df['time'] = df['time'].astype(float)
    return df