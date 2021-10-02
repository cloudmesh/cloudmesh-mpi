from mpi4py.futures import MPIPoolExecutor
import matplotlib.pyplot as plt
import numpy as np
from cloudmesh.common.StopWatch import StopWatch
import os

StopWatch.start("Overall time")

multiplier = os.getenv("multiplier")
workers = os.getenv("workers")

if multiplier:
    print(f"Proceeding since multiplier exists: {multiplier=}")
    multiplier = int(os.getenv("multiplier"))
    pass
else:
    print("No multiplier was input so multiplier defaults to 1")
    multiplier = 1
    pass
if workers:
    print(f"Proceeding since workers exists: {workers=}")
    workers = int(os.getenv("workers"))
    pass
else:
    print("No number of workers was input so workers defaults to 4")
    workers = 4
    pass

x0, x1, w = -2.0, +2.0, 640*multiplier
y0, y1, h = -1.5, +1.5, 480*multiplier
dx = (x1 - x0) / w
dy = (y1 - y0) / h

c = complex(0, 0.65)


def julia(x, y):
    z = complex(x, y)
    n = 255
    while abs(z) < 3 and n > 1:
        z = z**2 + c
        n -= 1
    return n


def julia_line(k):
    line = bytearray(w)
    y = y1 - k * dy
    for j in range(w):
        x = x0 + j * dx
        line[j] = julia(x, y)
    return line


if __name__ == '__main__':
    with MPIPoolExecutor(max_workers=workers) as executor:
        image = executor.map(julia_line, range(h))
        image = np.array([list(l) for l in image])
        plt.imsave("julia.png", image)

StopWatch.stop("Overall time")
StopWatch.benchmark()
