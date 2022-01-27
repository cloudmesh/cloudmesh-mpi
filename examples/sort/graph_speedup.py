from cloudmesh.common.util import readfile
from cloudmesh.common.Shell import Shell
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint

content = readfile("output-speedup.log").splitlines()
x = []
y = []
data = []
nums = []

# is this is wrongly calculated as the average has to be calculated first?
# should we have three graphs, one for values vs average(1), one for values vs min(1)  one for values vs max(1)
# count is const

#plots by speedup (n = 10000)
for p in range(1,12): #12 is # of processes on my computer
    n = 10000
    temp = []
    lines = Shell.find_lines_with(content, what=f"mergesort_{p}_")
    for entry in lines:
        values = entry.split(",")
        #x.append(p)
        #y.append(float(values[3]))
        #data.append([p, float(values[3])])
        temp.append(float(values[3]))
    nums.append(temp)
for p in range(1, 12):
    for cnt in range(10):
        x.append(p)
        y.append(float(nums[p-1][cnt] / nums[0][cnt]))
        data.append([p, float(nums[p-1][cnt] / nums[0][cnt])])

sns.set_theme(style="ticks", palette="pastel")
data = {
    "x":x,
    "y":y
}
ax = sns.boxplot(x="x", y="y",
data=data)
ax.set_title(f"speedup, size = {10000}")
ax.set_ylabel("speedup")
ax.set_xlabel("# of processes")
# sns.despine(offset=10, trim=True)
# plt.show()
plt.savefig('images/speedup.pdf')