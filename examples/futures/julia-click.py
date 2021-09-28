from mpi4py.futures import MPIPoolExecutor
import matplotlib.pyplot as plt
import numpy as np
from numba import jit
from cloudmesh.common.StopWatch import StopWatch
import click

StopWatch.start("Overall time")

global multiply

@click.command()
@click.option('--multiply', prompt='Input number that multiplies Julia picture resolution',
              type=int, default=1)
def run(multiply):
    global passer
    passer = multiply


x0, x1, w = -2.0, +2.0, 640 * passer
y0, y1, h = -1.5, +1.5, 480 * passer
dx = (x1 - x0) / w
dy = (y1 - y0) / h

c = complex(0, 0.65)


@jit(nopython=True)
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
    run()

    with MPIPoolExecutor() as executor:
        image = executor.map(julia_line, range(h))
        image = np.array([list(l) for l in image])
        plt.imsave("julia.png", image)

StopWatch.stop("Overall time")
StopWatch.benchmark()