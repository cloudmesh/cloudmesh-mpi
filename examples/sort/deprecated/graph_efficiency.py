import matplotlib.pyplot as plt
import seaborn as sns

from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import readfile

content = readfile("output-speedup.log").splitlines()
x = []
y = []
data = []
nums = []

# plots by efficiency (n = 10000)
for p in range(1, 12):  # 12 is # of processes on my computer
    n = 10000
    temp = []
    lines = Shell.find_lines_with(content, what=f"mergesort_{p}_")
    for entry in lines:
        values = entry.split(",")
        # x.append(p)
        # y.append(float(values[3]))
        # data.append([p, float(values[3])])
        temp.append(float(values[3]))
    nums.append(temp)
for p in range(1, 12):
    for cnt in range(10):
        x.append(p)
        speedup = float(nums[p - 1][cnt] / nums[0][cnt])
        y.append(speedup / p)
        data.append([p, speedup / p])

sns.set_theme(style="ticks", palette="pastel")
data = {
    "x": x,
    "y": y
}
ax = sns.boxplot(x="x", y="y",
                 data=data)
ax.set_title(f"efficiency, size = {10000}")
ax.set_ylabel("efficiency")
ax.set_xlabel("# of processes")
# sns.despine(offset=10, trim=True)
# plt.show()
plt.savefig('images/eficciency.pdf')
