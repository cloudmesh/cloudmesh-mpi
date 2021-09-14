from matplotlib import pyplot
from mpi4py import MPI
import numpy
from numba import jit
from cloudmesh.common.StopWatch import StopWatch


@jit(nopython=True)
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

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
if rank == 0:
    StopWatch.start(f'parallel {size}')
# number of rows to compute here
N = h // size + (h % size > rank)

# first row to compute here
start = comm.scan(N)-N

# array to store local result
Cl = numpy.zeros([N, w], dtype='i')


dx = (x2 - x1) / w
dy = (y2 - y1) / h
for i in range(N):
    y = y1 + (i+ start) * dy
    for j in range(w):
        x = x1 + j * dx
        Cl[i, j] = mandelbrot(x, y, maxit)

# gather results at root (process 0)

counts = comm.gather(N, root=0)
C = None
if rank == 0:
    C = numpy.zeros([h, w], dtype='i')

rowtype = MPI.INT.Create_contiguous(w)
rowtype.Commit()

comm.Gatherv(sendbuf=[Cl, MPI.INT],
             recvbuf=[C, (counts, None), rowtype],
             root=0)

rowtype.Free()

if rank == 0:
    StopWatch.stop(f'parallel {size}')

    pyplot.imshow(C, aspect='equal')
    pyplot.show()
    StopWatch.benchmark()



