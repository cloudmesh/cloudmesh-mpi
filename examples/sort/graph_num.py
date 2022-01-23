from cloudmesh.common.util import readfile
from cloudmesh.common.Shell import Shell
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint

content = readfile("output.log").splitlines()
x = []
y = []
data = []

#plots by size (n = 1000)
for p in range(1,12): #12 is # of processes on my computer
    n = 10000
    lines = Shell.find_lines_with(content, what=f"mergesort_{p}_")
    for entry in lines:
        values = entry.split(",")
        x.append(p)
        y.append(float(values[3]))
        data.append([p, float(values[3])])

sns.set_theme(style="ticks", palette="pastel")
data = {
    "x":x,
    "y":y
}
ax = sns.boxplot(x="x", y="y",
data=data)
ax.set_title(f"size = {n}")
ax.set_ylabel("time (s)")
ax.set_xlabel("# of processes")
sns.despine(offset=10, trim=True)
plt.show()