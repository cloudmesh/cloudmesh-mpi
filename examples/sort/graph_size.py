import matplotlib.pyplot as plt
import seaborn as sns

from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import readfile

content = readfile("output-speedup.log").splitlines()
x = []
y = []
data = []

# plots by process (p = 3)
for n in [10, 100, 1000, 10000]:
    p = 3
    lines = Shell.find_lines_with(content, what=f"mergesort_{p}_{n}")
    for entry in lines:
        values = entry.split(",")
        x.append(n)
        y.append(float(values[3]))
        data.append([n, float(values[3])])

sns.set_theme(style="ticks", palette="pastel")
data = {
    "x": x,
    "y": y
}
ax = sns.boxplot(x="x", y="y",
                 data=data)
ax.set_title(f"processes = {p}")
ax.set_ylabel("time (s)")
ax.set_xlabel("size of dataset")
# sns.despine(offset=10, trim=True)
# plt.show()
plt.savefig('images/size.pdf')
