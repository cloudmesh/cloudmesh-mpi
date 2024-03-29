# Towards Python MPI for Artificial Intelligence and Deep Learning Research 

Gregor von Laszewski,
Fidel Leal,
Erin Seliger,
Cooper Young,
Agness Lungu


## Preface

Add a preface

* Who we are and how this activity came about.

* Notation. We can copy what I have done in other books, but keep it
  simple e.g. we do not have to worry about epub

  * code
  * use of `verbatim` inline and in block
  * use of LaTex formulas
  * use of markdown
    * spaces before and after headline, itemize lists, e.g. online editors do that not correctly
    * hyperlinks
    * citation



## Overview

TODO: Gregor improves this section

After reflecting on the meeting I decided that in order to increase
your python knowledge and to also lead you towards research we will be
developing initially a tutorial that teaches students how to use MPI
(Message Passing Interface). We do this with something that is called
mpi4py. (later on we will use this to coordinate AI algorithms) We
will develop multiple sections to this tutorial and each of you will
each week work on a chapter so it can be redone by others. You can
also work together and share each others ideas and thoughts openly as
well as ask questions. We will do the following structured tasks (you
will need to know what plagiarism is and when and how you need to
cite):

## Hardware Considerations

Describes and summarizes what hardware you could use

### Backup

When you rock on a research project you may install programs on your
computer that's me cause problems at a later time. The work we do yes
research and not production. Hence, we need to be assuring that you
have a backup strategy in place before you work on your research
activities.

For that reason, we recommend that you purchase an external backup
drive that you use regularly to create backups from you are
System. The best Open backup solutions Orissa back up trash include
multiple redundant drives so that if even the backup fails you can
recover easily from a failure. An external backup drive is relatively
inexpensive and you can easily order them via internet vendors. To
protect yourself from a broken backup drive (this happens!) we
recommend either by at one point a second one or use a RAID-enabled
backup. Certainly your second or even primary backup could be a cloud
service such as google drive.

Alternatively and, you can use cloud storage services such as Google
Drive to back up your most important information.

Examples:

* USB Drive or External HDD enclosure with one or more disks, When
  using an SSD likely the fastest backup solution. YOU can buy also an
  external Drive bay with multiple bays and purcahse HDD or SSD drives
  based on your budget. Make sure to by one with USB3 or
  thunderbolt. The limit will be your budget.

* [TrueNas](https://www.truenas.com/) (you can build your own or get one ready made)

* [Synology](https://www.synology.com/en-us) (ready made)

* QNAS

### Bare metal on your Computer

TODO

Recommendations

* Memory (16GB)
* SSD (>512GB)

* Reasonably new computer less than 5 years of age

* Alternative culd be Raspberry PI4 with 8GB runnng Ubuntu or
  Raspberry OS for smaller projects. We have seen that some students
  had computers that cost when bought >$1K but because they were too
  old a Raspberry Pi of about $100 wass much much faster. It is up to
  you to make a decission which hardware you like to use. To get
  started with clusters and parallel computing ranging from MPI,
  Hadoop, SPark and containers a Raspberry PI cluster is not a bad
  choice

### Using Raspberry PIs

TODO

### Laptops and Desktops

TODO

### Virtual Machines

TODO requires >=16 GB on laptop/desktop

#### Multipass

#### WSL2

#### VMs on your local computer

#### Cloud Virtual Machines

#### Campus Resources

##### Indiana University

Computer and cluster at Indiana university could be alternative to
Raspberry PI cluster, but Cluster will teach you other things that you
will not experience if you use the campus cluster. You have more
access, please keep that in mind.

TODO: list resources hera nad how to get access

## Other resoources

* very important: <https://www.ismll.uni-hildesheim.de/lehre/prakAIML-17s/script/02.MPI.pdf>
* <https://materials.jeremybejarano.com/MPIwithPython/>
* <https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html>
* <https://research.computing.yale.edu/sites/default/files/files/mpi4py.pdf>
* <https://towardsdatascience.com/parallel-programming-in-python-with-message-passing-interface-mpi4py-551e3f198053>
* machinefile: <https://pythonprogramming.net/installing-testing-mpi4py-mpi-python-tutorial/>
* size, rank: <https://pythonprogramming.net/mpi4py-size-command-mpi/>
  they have mpirun.openmpi -np 5 -machinefile /home/pi/mpi_testing/machinefile python
  so we can specify a machine file, find out how that looks liek
* jupyter on mpi <https://raspi.farm/howtos/installing-MPI-on-the-cluster/>
* <https://pythonprogramming.net/basic-mpi4py-script-getting-node-rank/>
* <https://www.nesi.org.nz/sites/default/files/mpi-in-python.pdf>

## Installation 

In this section we will quickly summarize hwo you install of python on your hardware This includes 

* Windows 10
* MacOs
* Raspberry (using our cms burn)

Each installation documents the install from python.org

### Instalation on Windows 10

TODO

### Instalation on MacOS

TODO

### Instalation on Raspberry OS

TODO: using cms burn

### Instalation on Raspberry Ubuntu

TODO: using cms burn


## Introduction to MPI

* What is MPI and why do you want to use it

* What are some example MPI functionalities and usage patterns (send
  receive, embarrassing parallel

### Installation of mpi4py on Windows

1. Look up msmpi and click the second link to download and install msmpisetup.exe and msmpisdk.msi
3. Open the system control panel
4. Click on Advanced system settings and then Environment Variables
5. Under the user variables box click on Path
6. Click New in order to add C:\Program Files (x86)\Microsoft SDKs\MPI and C:\Program Files\Microsoft MPI\Bin to Path
7. Close any open bash windows and then open a new one
8. Type the command `which mpiexec`
9. Install mpi4py with `pip install mpi4py`
10. In order to verify that the installation worked type  `mpiexec -n 4 python mpi4py.bench helloworld`

### Installing mpi4py in a Raspberry Pi


1. Activate our virtual environment: `source ~/ENV3/bin/activate`
   
2. Install Open MPI in your pi by entering the following command:
   `sudo apt-get install openmpi-bin`.

   After installation is complete you can check if it was successful
   by using `mpicc --showme:version`.

3. Enter `pip install mpi4py` to download and install mpi4py.

4. The installation can be tested with `mpiexec -n 4 python -m
   mpi4py.bench helloworld` (depending on the number of cores/nodes
   available to you, it may be necessary to reduce the number of
   copies that follow the -n option) In a PI4, the above test
   returned:
   
   ```
   (ENV3) pi@red:~ $ mpiexec -n 4 python -m mpi4py.bench helloworld
   Hello, World! I am process 0 of 4 on red.
   Hello, World! I am process 1 of 4 on red.
   Hello, World! I am process 2 of 4 on red.
   Hello, World! I am process 3 of 4 on red.
   ```
   
### Installing mpi4py in MacOS
   
A similar process can be followed to install mpi4py in MacOS. In this
case, we can use Homebrew to get Open MPI by entering: `brew install
open-mpi`.
   
Once Open MPI is working, steps 3 and 4 from the above pi4
installation can be followed in order to download and install mpi4py.

## Hello World

To test if it works a build in test program is available.

To run it on on a single host with n cores (lest assume you have 2
cores), you can use:

```
mpiexec -n 4 python -m mpi4py.bench helloworld
Hello, World! I am process 0 of 5 on localhost.
Hello, World! I am process 1 of 5 on localhost.
Hello, World! I am process 2 of 5 on localhost.
Hello, World! I am process 3 of 5 on localhost.
```

Note that the messages can be in different order.


To run it on mulitple hosts with each having n cores please create a
hostfile as follows:

TODO:






## Machine file, hostfile, rankfile


Run sudo apt-get install -y python-mpi4py on all nodes.

Test the installation: mpiexec -n 5 python -m mpi4py helloworld

THIS CAN BE DONE BEST WITH CLOUDMESH

FIRTS TEST BY HAND

TODO: VERIFY 

```
mpirun.openmpi -np 2 \
               -machinefile /home/pi/mpi_testing/machinefile \
               python helloworld.py
```

The machinefile contains the ipaddresses

```
pi@192. ....
yout add teh ip addresses
```

TODO: learn about and evaluate and test if we can do 

```
mpirun -r my_rankfile --report-bindings ... 

Where the rankfile contains:
rank 0=compute17 slot=1:0
rank 1=compute17 slot=1:1
rank 2=compute18 slot=1:0
rank 3=compute18 slot=1:1
```

## MPI Functionality examples

### MPI Collective Communication functionality examples

#### Broadcast `comm.bcast()`

In this example, we broadcast a two-entry Python dictionary from a
root process to the rest of the processes in our communicator group.

``` python
from mpi4py import MPI

# Communicator
comm = MPI.COMM_WORLD

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

# Process with rank 0 gets the data to be broadcast
if rank == 0:
    data = {'size' : [1,3,8],
            'name' : ['disk1', 'disk2', 'disk3']}

# Other processes' data is empty
else:
    data = None

# Print data in each process
print("before broadcast, data on rank %d is "%comm.rank, data)

# Data from process with rank 0 is broadcast to other processes in our
# communicator group
data = comm.bcast(data, root=0)

# Print data in each process after broadcast
print("after broadcast, data on rank %d is "%comm.rank, data)

```

After running `mpiexec -n 4 python bcast.py` we get the following:

```
before broadcast, data on rank 0 is  {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
before broadcast, data on rank 1 is  None
before broadcast, data on rank 2 is  None
before broadcast, data on rank 3 is  None
after broadcast, data on rank 0 is  {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
after broadcast, data on rank 1 is  {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
after broadcast, data on rank 2 is  {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
after broadcast, data on rank 3 is  {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
```
As we can see, the process with rank 1, received the data broadcast from rank 0.


#### Scatter `comm.scatter()`

In this example, with scatter the members of a list among the
processes in the communicator group.

``` python
from mpi4py import MPI

# Communicator
comm = MPI.COMM_WORLD

# Number of processes in the communicator group
size = comm.Get_size()

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

# Process with rank 0 gets a list with the data to be scattered
if rank == 0:
    data = [(i+1)**2 for i in range(size)]
else:
    data = None

# Print data in each process
print("before scattering, data on rank %d is "%comm.rank, data)

# Scattering occurs
data = comm.scatter(data, root=0)

# Print data in each process after scattering
print("data for rank %d is "%comm.rank, data)
```

Executing `mpiexec -n 4 python scatter.py` yields:

```
before scattering, data on rank 2 is  None
before scattering, data on rank 3 is  None
before scattering, data on rank 0 is  [1, 4, 9, 16]
before scattering, data on rank 1 is  None
data for rank 2 is  9
data for rank 1 is  4
data for rank 3 is  16
data for rank 0 is  1
```

The members of the list from process 0 have been successfully
scattered among the rest of the processes in the communicator group.


#### Gather `comm.gather()`

In this example, data from each process in the communicator group is
gathered in the process with rank 0.


``` python
from mpi4py import MPI

# Communicator
comm = MPI.COMM_WORLD

# Number of processes in the communicator group
size = comm.Get_size()

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

# Each process gets different data, depending on its rank number
data = (rank+1)**2

# Print data in each process
print("before gathering, data on rank %d is "%comm.rank, data)

# Gathering occurs
data = comm.gather(data, root=0)

# Process 0 prints out the gathered data, rest of the processes
# print their data as well
if rank == 0:
    print("after gathering, process 0's data is ", data)
else:
    print("after gathering, data in rank %d is "%comm.rank, data)
```

Executing `mpiexec -n 4 python gather.py` yields:

```
before gathering, data on rank 2 is  9
before gathering, data on rank 3 is  16
before gathering, data on rank 0 is  1
before gathering, data on rank 1 is  4
after gathering, data in rank 2 is  None
after gathering, data in rank 1 is  None
after gathering, data in rank 3 is  None
after gathering, process 0's data is  [1, 4, 9, 16]
```

The data from processes with rank `1` to `size - 1` have been
successfully gathered in process 0.


#### Broadcasting buffer-like objects `comm.Bcast()`

In this example, we broadcast a NumPy array from process 0 to the rest
of the processes in the communicator group.

``` python
from mpi4py import MPI
import numpy as np

# Communicator
comm = MPI.COMM_WORLD

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

# Rank 0 gets a NumPy array containing values from 0 to 9
if rank == 0:
    data = np.arange(0,10,1, dtype='i')

# Rest of the processes get an empty buffer
else:
    data = np.zeros(10, dtype='i')

# Print data in each process
print("before broadcasting, data for rank %d is: "%comm.rank, data)

# Broadcast occurs
comm.Bcast(data, root=0)

# Print data in each process after broadcast
print("after broadcasting, data for rank %d is: "%comm.rank, data)
```

Executing `mpiexec -n 4 python npbcast.py` yields:

```
before broadcasting, data for rank 1 is:  [0 0 0 0 0 0 0 0 0 0]
before broadcasting, data for rank 2 is:  [0 0 0 0 0 0 0 0 0 0]
before broadcasting, data for rank 3 is:  [0 0 0 0 0 0 0 0 0 0]
before broadcasting, data for rank 0 is:  [0 1 2 3 4 5 6 7 8 9]
after broadcasting, data for rank 0 is:  [0 1 2 3 4 5 6 7 8 9]
after broadcasting, data for rank 2 is:  [0 1 2 3 4 5 6 7 8 9]
after broadcasting, data for rank 3 is:  [0 1 2 3 4 5 6 7 8 9]
after broadcasting, data for rank 1 is:  [0 1 2 3 4 5 6 7 8 9]
```

As we can see, the values in the array at process with rank 0 have
been broadcast to the rest of the processes in the communicator group.


#### Scattering buffer-like objects `comm.Scatter()`

In this example, we scatter a NumPy array among the processes in the
communicator group.

``` python
from mpi4py import MPI
import numpy as np

# Communicator
comm = MPI.COMM_WORLD

# Number of processes in the communicator group
size = comm.Get_size()

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

# Data to be sent
sendbuf = None

# Process with rank 0 populates sendbuf with a 2-D array,
# based on the number of processes in our communicator group
if rank == 0:
    sendbuf = np.zeros([size, 10], dtype='i')
    sendbuf.T[:,:] = range(size)
    
    # Print the content of sendbuf before scattering
    print('sendbuf in 0: ', sendbuf)

# Each process getd a buffer (initially containing just zeros) 
# to store scattered data.
recvbuf = np.zeros(10, dtype='i')

# Print the content of recvbuf in each process before scattering
print('recvbuf in  %d: '%rank, recvbuf)

# Scattering occurs
comm.Scatter(sendbuf, recvbuf, root=0)

# Print the content of sendbuf in each process after scattering
print('Buffer in process %d contains: '%rank, recvbuf)
```

Executing `mpiexec -n 4 python npscatter.py` yields:

```
recvbuf in  1:  [0 0 0 0 0 0 0 0 0 0]
recvbuf in  2:  [0 0 0 0 0 0 0 0 0 0]
recvbuf in  3:  [0 0 0 0 0 0 0 0 0 0]
sendbuf in 0:  [[0 0 0 0 0 0 0 0 0 0]
 [1 1 1 1 1 1 1 1 1 1]
 [2 2 2 2 2 2 2 2 2 2]
 [3 3 3 3 3 3 3 3 3 3]]
recvbuf in  0:  [0 0 0 0 0 0 0 0 0 0]
Buffer in process 2 contains:  [2 2 2 2 2 2 2 2 2 2]
Buffer in process 0 contains:  [0 0 0 0 0 0 0 0 0 0]
Buffer in process 3 contains:  [3 3 3 3 3 3 3 3 3 3]
Buffer in process 1 contains:  [1 1 1 1 1 1 1 1 1 1]
```

As we can see, the values in the 2-D array at process with rank 0,
have been scattered among all our processes in the communicator group,
based on their rank value.


#### Gathering buffer-like objects `comm.Gather()`

In this example, we gather a NumPy array from the processes in the
communicator group into a 2-D array in process with rank 0.

``` python
from mpi4py import MPI
import numpy as np

# Communicator group
comm = MPI.COMM_WORLD

# Number of processes in the communicator group
size = comm.Get_size()

# Get the rank of the current process in the communicator group
rank = comm.Get_rank()

# Each process gets an array with data based on its rank.
sendbuf = np.zeros(10, dtype='i') + rank

# Print the data in sendbuf before gathering 
print('Buffer in process %d before gathering: '%rank, sendbuf)

# Variable to store gathered data
recvbuf = None

# Process with rank 0 initializes recvbuf to a 2-D array conatining
# only zeros. The size of the array is determined by the number of
# processes in the communicator group
if rank == 0:
    recvbuf = np.zeros([size,10], dtype='i')

    # Print recvbuf
    print('recvbuf in process 0 before gathering: ', recvbuf) 

# Gathering occurs
comm.Gather(sendbuf, recvbuf, root=0)

# Print recvbuf in process with rank 0 after gathering
if rank == 0:
        print('recvbuf in process 0 after gathering: \n', recvbuf)
```
       
Executing `mpiexec -n 4 python npgather.py` yields:

```
Buffer in process 2 before gathering:  [2 2 2 2 2 2 2 2 2 2]
Buffer in process 3 before gathering:  [3 3 3 3 3 3 3 3 3 3]
Buffer in process 0 before gathering:  [0 0 0 0 0 0 0 0 0 0]
Buffer in process 1 before gathering:  [1 1 1 1 1 1 1 1 1 1]
recvbuf in process 0 before gathering:  [[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
recvbuf in process 0 after gathering: 
 [[0 0 0 0 0 0 0 0 0 0]
 [1 1 1 1 1 1 1 1 1 1]
 [2 2 2 2 2 2 2 2 2 2]
 [3 3 3 3 3 3 3 3 3 3]]
```

The values contained in the buffers from the different processes in
the group have been gathered in the 2-D array in process with rank 0.


#### send receive

TODO

#### Dynamic Process Management

TODO

#### task processing (spwan, pull, …)


TODO: Cooper

##### Futures

<https://mpi4py.readthedocs.io/en/stable/mpi4py.futures.html>

#### examples for other collective communication methods

TODO

## MPI-IO

TODO: Agnes

### Collective I/O with NumPy arrays

TODO: Agnes

### Non-contiguous Collective I/O with NumPy arrays and datatypes

TODO: Agnes


## Monte Carlo calculation of Pi

TODO: Open, improve

TODO WHAT IS THE PROBLEM GOAL

We start with the Mathematical formulation of the Monte Carlo
calulation of pi. For each quadrant of the unit square, the area is
pi.  Therefore, the ratio of the area outside of the circle is pi over
four.  With this in mind, we can use the Monte Carlo Method for the
calculation of pi.

TODO: Drawing

TODO: HOW AND WHY DO WE NEED MULTIPLE COMPUTERS

### Program

TODO: Open



* Example program to run Montecarlo on multiple hosts

* Benchmarking of the code
  * cloudmesh.common (not thread safe, but still can be used, research how to use it in multiple threads)
  * other strategies to benchmark, you research (only if really needed
* Use numba to speed up the code
  * describe how to install
* showcase basic usage on our monte carlo function
* display results with matplotlib


## GPU Programming with MPI

Only possibly for someone with GPU (contact me if you do) Once we are
finished with MPI we will use and look at python dask and other
frameworks as well as rest services to interface with the mpi
programs. This way we will be able to expose the cluster to anyone and
they do not even know they use a cluster while exposing this as a
single function … (edited)

The github repo is used by all of you to have write access and
contribute to the research effort easily and in parallel.  You will
get out of this as much as you put in. Thus it is important to set
several dedicated hours aside (ideally each week) and contribute your
work to others.

It is difficult to asses how long the above task takes as we just get
started and we need to learn first how we work together as a team. If
I were to do this alone it may take a week, but as you are less
experienced it would likely take longer. However to decrease the time
needed we can split up work and each of you will work on a dedicated
topic (but you can still work in smaller teams if you desire). We will
start assigning tasks in github once this is all set up.

Idea:

WE WILL NO LONGER USE HACKMD AS GITHUB IS BETTER FOR INTEGRATION WITH
CODE

* tutorial about hackmd.io <https://hackmd.io/t9SkKiSLR5qW9RUUA_CT-A>
* Github vs hackmd

We will use initially hackmd so we avoid issues with github and we can
learn github once we do more coding.
