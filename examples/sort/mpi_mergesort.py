import numpy as np
from mpi4py import MPI
from mpi4py import MPI
import random
import numpy as np
from cloudmesh.common.StopWatch import StopWatch

READY, START, DONE, EXIT = 0, 1, 2, 3

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank
status = MPI.Status()

def sequential_merge(l,r):
    size_1 = len(l) 
    size_2 = len(r) 
  
    res = [] 
    i, j = 0, 0
  
    while i < size_1 and j < size_2: 
        if l[i] < r[j]:   
          res.append(l[i]) 
          i += 1
  
        else: 
          res.append(r[j]) 
          j += 1
  
    res = res + l[i:] + r[j:]
    return res 

def split(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

def send_data():
    # add loop??
    comm.send(None, dest=0, tag=READY)
    task = []
    
    task = comm.recv(source=0, tag=MPI.ANY_TAG, status=status)
    tag = status.Get_tag()

    # need to separate by tag
    task = sorted(task)
    comm.send(list(task), dest=0, tag=DONE)



def producer(chunk,process):
    arraySize = 100000
    data = np.arange(1,arraySize)
    random.shuffle(data)
    data = list(data)
    smalldata = split(data, chunk)

    finallist = []
    start = 0
    end = chunk
    for i in range(1, process):
        comm.send(smalldata[i-1], dest=i, tag=START)
        #comm.send(1, dest=i, tag=START)
        
    # need to merge all lists when done

    print(finallist)
                

if __name__=="__main__":
    StopWatch.start("MPI merge sort")
    if rank == 0:
        chunk = 32
        process = 4 
        producer(chunk, process)
        for loop in range(1,process):
            comm.send(None, dest=loop, tag=EXIT)
        StopWatch.stop("MPI merge sort")      
    else:
        send_data()

    StopWatch.benchmark()

  
