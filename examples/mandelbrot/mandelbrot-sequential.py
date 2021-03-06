from matplotlib import pyplot
from cloudmesh.common.StopWatch import StopWatch

StopWatch.start("Overall time")

def mandelbrot(x, y, maxit):
    c = x + y*1j
    z = 0 + 0j
    it = 0
    while abs(z) < 2 and it < maxit:
        z = z**2 + c
        it += 1
    return it

x1, x2 = -2.0, 1.0
y1, y2 = -1.0, 1.0
w, h = 1200, 800
maxit = 127

import numpy
C = numpy.zeros([h, w], dtype='i')
dx = (x2 - x1) / w
dy = (y2 - y1) / h
for i in range(h):
    y = y1 + i * dy
    for j in range(w):
        x = x1 + j * dx
        C[i, j] = mandelbrot(x, y, maxit)


pyplot.imsave('mandelbrot-sequential.png', C)
pyplot.imsave('mandelbrot-sequential.pdf', C)

StopWatch.stop("Overall time")
StopWatch.benchmark()


