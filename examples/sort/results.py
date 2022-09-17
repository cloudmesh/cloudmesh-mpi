import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from cloudmesh.common.util import banner
from analysis import get_data
from analysis import read_log, read_logs
from analysis import generate_average

user = "alex"
node = "2400MHz"
sorts = ["seq-merge", "mp-mergesort"]
sort = "mp-mergesort"

sizes = [100, 1000, 10e4, 10e5]
sizes = [int(size) for size in sizes]

# this will take a long time. 
# also if you don't want to use all your processors then use different commands. 
# for sort in sorts:
    # for size in sizes:
        # run_cmd = f"./run.py --user={user} --node={node} --size={size} --sort={sort}"
        # banner(run_cmd)
        # os.system(run_cmd)


files = ["alex"]
sorts = ["seq-merge", "mp-mergesort"]

frames = []
for file in files:
    for sort in sorts:
        frame = []
        for size in sizes: 
            size = int(size)
            log = f'{sort}-{node}-{file}'
            _frame = read_log(log, size=size, tag=sort)
            frame = frame + _frame
        frames.append(frame)
# print(frames)


df = pd.DataFrame()
for frame in frames:
    _df = pd.DataFrame(data=frame,
                columns=["processes", "time", "size", "name", "tag"])
    df = pd.concat([df, _df], ignore_index=True)
# plot_benchmark_by_size(df, "name", tag=sort, files=files, x="size", y="time")

df = df.pivot_table(
    values='time', index=['tag', 'processes'], columns=['name', 'size'], fill_value=0, aggfunc='mean')
speedup = df.rdiv(df.loc['seq-merge'].iloc[0])
print(speedup)