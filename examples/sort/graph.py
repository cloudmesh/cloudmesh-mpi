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
for p in range(1,12):
    for n in [10, 100, 1000]:
        lines = Shell.find_lines_with(content, what=f"mergesort_{n}_")
        for entry in lines:
            values = entry.split(",")
            x.append(n)
            y.append(float(values[3]))
            data.append([n, float(values[3])])


#plt.scatter(x, y)
#plt.xlabel('N')
#plt.ylabel('Time/s')
#plt.show()

sns.set_theme(style="ticks", palette="pastel")
data = {
    "x":x,
    "y":y
}
# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="x", y="y",
            data=data)
sns.set_title(f"{")
sns.despine(offset=10, trim=True)
plt.show()