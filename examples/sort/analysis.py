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
    lines = Shell.find_lines_with(content, "# csv")[1:]

    for line in lines:
        line = line.replace("'", '"')
        data = "{" + line.split("{")[1].split("},")[0] + "}"
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

def generate_average(df, sort=None, size=None, name=None):
    _df = df.loc[(df['name'] == name) & (df['sort'] == sort) &  (df['size'] == size) ]
    avg = _df.groupby(['processors', 'name', 'size', 'sort']).mean()
    avg['sort'] = sort
    avg['name'] = name
    return avg

def generate_df():
    directory = "log"
    all_data = []
    for file in os.listdir(directory):
        f = os.path.join(directory, file)
        all_data.extend(read_log(f))

    df = pd.DataFrame(all_data)
    df['time'] = df['time'].astype(float)
    return df

def average_df(df):
    _df = df.groupby(['p', 'size', 'repeat', 'sort', 'user', 'node', 't', 'c'])['time'].mean()
    _df.reset_index()
    return _df


log = "mp-v100-alex-50-9-None-None.log"
print(read_log(log))