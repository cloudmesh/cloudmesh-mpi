# Preface

in part published at

* Medium <https://laszewski.medium.com/python-and-mpi-part-1-7e76a6ec1c6d>
* Frinds Link: <https://laszewski.medium.com/python-and-mpi-part-1-7e76a6ec1c6d?sk=cc21262764659c0ef2d3ddc684f54034>

## Document Management in GitHub


**Note:** The source document is managest at
<https://cloudmesh.github.io/cloudmesh-mpi/doc/chapters>
To make changes or corrections please use a pull request

The repository, documentation, and examples are available at:

* Repository: <https://github.com/cloudmesh/cloudmesh-mpi>
* Examples: <https://github.com/cloudmesh/cloudmesh-mpi/tree/main/examples>
* Documents: 
  * <https://cloudmesh.github.io/cloudmesh-mpi/report-mpi.pdf>
  * <https://cloudmesh.github.io/cloudmesh-mpi/report-group.pdf>
    
To check out the repository use 
  
```
$ git clone git@github.com:cloudmesh/cloudmesh-mpi.git
```

or 
  
```
$ git clone https://github.com/cloudmesh/cloudmesh-mpi.git
```


## Document Notation

To keep things uniform, we use the following document notations.

1. Empty lines are to be placed before and after a context change, such
   as a headline, paragraph, list, image inclusion.

2. All code is written in code blocks using and three backquotes. A rendered example looks as follows:

   ```
   this is an example
   ```

3. Single quote inclusion must be used for filenames and other names
   as they are referred to in code blocks.

4. To showcase command inclusion, we use a block but precede every command 
   with a `$` or other prefix indicating the computer on which the command 
   is executed. 
   
   ```
   $ ls 
   ```
   
5. bibliography is managed via footnotes


# Introduction

(Same as abstract): Today Python has become the predominantly
programming language to coordinate scientific applications, especially
machine and deep learning applications. However, previously existing
parallel programming paradigms such as **Message Passing Interface
(MPI)** have proven to be a useful asset when it comes to enhancing
complex data flows while executing them on multiple computers
, including supercomputers. The framework is well known in the
C-language community.  However, many practitioners do not have the time
to learn C to utilize such advanced cyberinfrastructure. Hence, it is
advantageous to access MPI from Python. We showcase how you can easily
deploy and use MPI from Python via a tool called `mpi4pi`.  

Message Passing Interface (MPI) is a message-passing standard that
allows for efficient data communication between the address spaces
of multiple processes. The MPI standard began in 1992 as a collective
effort by several organizations, institutions, vendors, and
users. Since the first draft of the specification in November 1993,
the standard has undergone several revisions and updates leading to
its current version: MPI 4.0 (June 2021).

Multiple implementations following the standard exist, including the two most popular MPICH [^MPICH] and OpenMPI [^OPENMPI].  However, other free or
commercial implementations exist [^MISSINGMPI].

Additionally, MPI is a language-independent interface. Although support for C and Fortran is
included as part of the standard, multiple libraries providing bindings for other languages
are available, including those for Java, Julia, R, Ruby, and Python.

Thanks to its user-focused abstractions, its standardization,
portability, and scalability, and availability MPI is a popular tool
in the creation of high-performance and parallel computing programs.

# Installation

Next, we discuss how to install mpi4p on various systems. We will focus on installing it on a single computer using multiple cores.


## Getting the CPU Count

For the examples listed in this document, knowing the number of
cores on your computer is important. This can be found out through the command line or a python program.

In Python, you can do it with 

```python
import multiprocessing
multiprocessing.cpu_count()
```

or as a command line 

```bash
$ python -c "import multiprocessing;  print(multiprocessing.cpu_count())"
```

However, you can also use the command line tools that we have included in our documentation.

## Windows 10 EDU or PRO

*Note:* We have not tested this on Windows home.

1. We assume you have installed GitBash on your computer. The installation is easy, but be careful to watch the various options at install time.
   Make sure it is added to the Path variable.

   For details see: <https://git-scm.com/downloads>

2. We also assume you have installed Python3.9 according to either the installation at python.org or conda. We do recommend the installation
   from python.org.

   <https://www.python.org/downloads/>

   You will need to install a python virtual env to avoid conflict by accident with your system installed version of Python.

   For details on how to do this, please visit our extensive documentation at [???]

1. Microsoft has its own implementation of MPI which we recommend at this time. First, you need to download msmpi from

   *
   <https://docs.microsoft.com/en-us/message-passing-interface/microsoft-mpi#ms-mpi-downloads>
   
   Go to the download link underneath the heading `MS-MPI Downloads`
   and download and install it. Select the two packages and click 
   Next. When downloaded, click on them and complete the setups.

   ```
   msmpisetup.exe
   msmpisdk.msi
   ```

2. Open the system control panel and click on `Advanced system settings` (which
   can be searched for with the search box in the top-right, and then click
   `View advanced system settings`) and then click `Environment Variables...`

3. Under the user variables box, click on `Path`

4. Click New in order to add

   `C:\Program Files (x86)\Microsoft SDKs\MPI`

   and

   `C:\Program Files\Microsoft MPI\Bin`

   to the Path. The `Browse Directory...`
   button makes this easier, and the `Variable name` can correspond to each
   directory, e.g., "MPI" and "MPI Bin" respectively

5. Close any open bash windows and then open a new one

6. Type the command

   ```bash
   $ which mpiexec
   ```

   to verify if it works.

7. After you verified it is available, install mpi4py with

   ```bash
   $ pip install mpi4py
   ```

   ideally, while bash is in venv

8. Next, find out how many processes you can run on your machine and remember that number. You can do this with

   ```bash
   $ wmic CPU Get DeviceID,NumberOfCores,NumberOfLogicalProcessors
   ```

   Alternatively, you can use a python program as discussed in the section "Getting the CPU Count"

## macOS

1. Find out how many processes you can run on your machine and remember that number. You can do this with

   ```bash
   $ sysctl hw.physicalcpu hw.logicalcpu
   ```

2. First, install python 3 from <https://www.python.org/downloads/>

3. Next, install homebrew and install the open-mpi version of MPI as well as mpi4py:

   ```
   $ xcode-select --install
   $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   $ brew install wget
   $ brew install open-mpi
   $ python3 -m venv ~/ENV3
   $ source ~/ENV3/bin/activate
   $ pip install mpi4py
   ```

## Ubuntu

These instructions apply to 20.04 and 21.04. Please use 20.04 in case you like to use GPUs.

1. First, find out how many processes you can run on your machine and remember that number. You can do this with

   ```bash
   $ nproc
   ```

2. The installation of mpi4py on Ubuntu is relatively easy. Please
   follow these steps. We recommend that you create a python `venv` so
   you do not by accident interfere with your system python. As usual,
   you can activate it in your `.bashrc` file while adding the source
   line there. Lastly, make sure you check it out and adjust the `-n`
   parameters to the number of cores of your machine. In our example,
   we have chosen the number 4, you may have to change that value

   ```bash
   $ sudo apt install python3.9 python3.9-dev
   $ python3 -m venev ~/ENV3
   $ source `/ENV3/bin/activate`
   (ENV3) $ sudo apt-get install -y mpich-doc mpich 
   (ENV3) $ pip install mpi4py -U
   ```

## Raspberry Pi
   
1. Install Open MPI in your pi by entering the following command assuming a PI4, PI3B+ PI3, PI2:
   
   ```bash
   $ python -m venv ~/ENV3
   $ source ~/ENV3/bin/activate
   $ sudo apt-get install openmpi-bin
   $ mpicc --showme:version
   $ pip install mpi4py
   ```

   If you have other Raspberry Pi's you may need to update the core count according to the hardware specification. 

## Testing the Installation

On all systems, the installation is very easy. Just change in our example the number 4 to the number of cores in your system.

   ```bash
   (ENV3) $ mpiexec -n 4 python -m mpi4py.bench helloworld   
   ```

You will see an output similar to 

   ```
   Hello, World! I am process 0 of 4 on myhost.
   Hello, World! I am process 1 of 4 on myhost.
   Hello, World! I am process 2 of 4 on myhost.
   Hello, World! I am process 3 of 4 on myhost.
   ```

where `myhost` is the name of your computer.

***Note:** the messages can be in a different order*.


# Hosts, Machinefile, Rankfile

## Running MPI on a Single Computer

In case you like to try out MPI and just use it on a single computer
with multiple cors, you can skip this section for now and revisit it,
once you scale up and use multiple computers.

## Running MPI on Multiple  Computers

MPI is designed for running programs on multiple computers. One of
these computers serves as manager and communicates to its workers. To
define on which computer is running what, we need to have a
a configuration file that lists a number of hosts to participate in our
set of machines, the MPI cluster.

The configuration file specifying this is called a machinefile
or rankfile. We will explain the differences to them in this
section.

### Prerequisite

Naturally, the requisite to use a cluster is that you

1. have MPI and mpi4py installed on each of the computers, and
2. have access via ssh on each of these computers

If you use a Raspberry PI cluster, we recommend using our
cloudmesh-pi-burn program [TODOREF]. This will conveniently create you
a Raspberry PI cluster with login features established. You still
need to install mpi4py, however on each node.

If you use another set of resources, you will often see the
recommendation to use passwordless ssh key between the nodes. This we
only recommend if you are an expert and have placed the cluster behind
a firewall. If you experiment instead with your own cluster, we
recommend that you use password-protected SSH keys on your manager
node and populate them with ssh-copy-id to the worker computers. To
not always have to type in your password to the different machines, we
recommend you use `ssh-agent`, and `ssh-add`.


### Using Hosts

In the case of multiple computers, you can simply specify the hosts as a
parameter to your MPI program that you run on your manager node


   ```bash
   (ENV3) $ mpiexec -n 4 -host re0,red1,red2,red3 python -m mpi4py.bench helloworld   
   ```

To specify how many processes you like to run on each of them, you can use the option `-ppn` followed by the number.

   ```bash
   (ENV3) $ mpiexec -n 4 -pn 2 -host re0,red1,red2,red3 python -m mpi4py.bench helloworld   
   ```

As today we usually have multiple cores on a processor, you could be using that core count as the parameter.


### Machinefile 

To simplify the parameter passing to MPI you can use machine files
instead.  This allows you also to define different numbers of
processes for different hosts. Thus it is more flexible. In fact, we
recommend that you use a machine file in most cases as you then also
have a record of how you configured your cluster.

The machine file is a simple text file that lists all the different
computers participating in your cluster. As MPI was originally
designed at a time when there was only one core on a computer, the
simplest machine file just lists the different computers. When
starting a program with the machine file as option, only one core of
the computer is utilized.

The machinefile can be explicitly passed along as a parameter while
placing it in the manager machine

```
mpirun.openmpi \
  -np 2 \
  -machinefile /home/pi/mpi_testing/machinefile \
  python helloworld.py
```
 
An example of a simple machinefile contains the IP addresses. The
username can be proceeded by the IP address.

```
pi@192.168.0.10:1
pi@192.168.0.11:2
pi@192.168.0.12:2
pi@192.168.0.13:2
pi@192.168.0.14:2
```

In many cases, your machine name may be available within your network and known to all hosts in the cluster. In that case, it is more convenient.
To sue the machine names.

```
pi@red0:1
pi@red1:2
pi@red2:2
pi@red3:2
pi@red4:2
```

Please make sure to change the IP addresses or name of your hosts according to
your network.

### Rankfiles for Multiple Cores

In contrast to the host parameter, you can fine-tune the placement of
processes to computers with a `rankfile`. This may be important if your hardware has, for
example specific computers for data storage or GPUs.

If you like to add multiple cores from a machine, you can also use a
`rankfile`


```
mpirun -r my_rankfile --report-bindings ... 

Where the rankfile contains:
rank 0=pi@192.168.0.10 slot=1:0
rank 1=pi@192.168.0.10 slot=1:1
rank 2=pi@192.168.0.11 slot=1:0
rank 3=pi@192.168.0.10 slot=1:1
```

In this configuration, we only use 2 cores from two different PIs.


# MPI Functionality

In this section, we will discuss several useful MPI communication features. 

## Differences to the C Implementation of MPI

Before we start with a detailed introduction, we like to make those
that have experience with non Python versions of MPI aware of some
differences.

### Initialization

In mpi4py, the standard MPI_INIT() and MPI_FINALIZE() commonly used to
initialize and terminate the MPI environment are automatically handled
after importing the mpi4py module.  Although not generally advised,
mpi4py still provides MPI.Init() and MPI.Finalize() for users
interested in manually controlling these operations. Additionally, the
automatic initialization and termination can be deactivated. For more
information on this topic, please check the original mpi4py documentation:

 * [MPI.Init() and MPI.Finalize()](https://githubmemory.com/repo/mpi4py/mpi4py/issues/54)
 * [Deactivating automatic initialization and termination on mpi4py](https://bitbucket.org/mpi4py/mpi4py/issues/85/manual-finalizing-and-initializing-mpi)

### Capitalization for Pickle vs. Memory Messages

Another characteristic feature of mpi4py is the availability of
uppercase and lowercase communication methods. Lowercase methods like
`comm.send()` use Python's `pickle` module to transmit objects in a
serialized manner. In contrast, the uppercase versions of methods like
`comm.Send()` enable transmission of data contained in a contiguous
memory buffer, as featured in the MPI standard. For additional
information on the topic, the manual section 
[Communicating Python Objects and Array Data](https://mpi4py.readthedocs.io/en/stable/overview.html?highlight=pickle#communicating-python-objects-and-array-data).

## MPI Functionality

### Communicator

All MPI processes need to be addressable and are grouped in a `communicator`. The default communicator is called `world` and assigns a rank to each process within the communicator.

Thus all MPI programs we will discuss here start with

```python
comm = MPI.COMM_WORLD
```

In the MPI program, the function

```python
rank = comm.Get_rank()
```

returns the rank. This is useful to be able to write conditional
programs that depend on the rank. Rank `0` is the rank of the manager process.



### Point-to-Point Communication

#### Send and Recieve Python Objects

The `send()` and `recv()` methods provide for functionality to transmit data
between two specific processes in the communicator group. It can be applied to any Python data object that can be pickled. The advantage is that the object is preserved, however it comes with the disadvantage that pickling the data takes more time than a direct memory copy.


![Sending and receiving data between two processes](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/send_receive.png){ width=50% }


Here is the definition for the `send()` method:

```python
comm.send(buf, dest, tag)
```

`buf` represents the data to be transmitted, `dest` and `tag` are integer
values that specify the rank of the destination process, and a tag to identify
the message being passed, respectively. `tag` is particularly useful for cases
when a process sends multiple kinds of messages to another process.

On the other end is the `recv()` method, with the following definition:

```python
comm.recv(buf, source, tag, status)
```    

In this case, `buf` can specify the location for the received data to
be stored. In more recent versions of MPI, 'buf' has been
deprecated. In those cases, we can simply assign `comm.recv(source,
tag, status)` as the value of our buffer variable in the receiving
process. Additionally, `source` and `tag` can specify the desired
source and tag of the data to be received. They can also be set to
`MPI.ANY_SOURCE` and `MPI.ANY_TAG`, or be left unspecified.

In the following example, an integer is transmitted from process 0 to
process 1.

``` python
!include ../examples/send_receive.py
```

Executing `mpiexec -n 4 python send_receive.py` yields:

```bash
After send/receive, the value in process 2 is None
After send/receive, the value in process 3 is None 
After send/receive, the value in process 0 is None
After send/receive, the value in process 1 is 42
```

As we can see, the transmission only occurred between processes 0 and 1, and
no other process was affected.

#### Send and Recive Python Memory Objects

The following example illustrates the use of the uppercase versions of
the methods `comm.Send()` and `comm.Recv()` to perform a transmission
of data between processes from memory to memory. In our example we
will agian be sending a message between processors of rank 0 and 1 in
the communicator group.

```python
!include ../examples/send_receive_buffer.py
```

Executing `mpiexec -n 4 python send_receive_buffer.py` yields:

```bash
After Send/Receive, the value in process 3 is [0 0 0 0 0]
After Send/Receive, the value in process 2 is [0 0 0 0 0]
After Send/Receive, the value in process 0 is [0 0 0 0 0]
After Send/Receive, the value in process 1 is [1 2 3 4 5]
```

#### Non-blocking send and Recieve

MPI can also use non-blocking communications. This allows the program
to send the message without waiting for the completion of the
submission. This is useful for many parallel programs so we can
overlap communication and computation while both take place
simultaneously. The same can be done with receive, but if a message is
not available and you do need the message, you may have to probe or even use a blocked receive.  To wait for
a message to be sent or received, we can also use the wait method
, effectively converting the non-blocking message to a blocking one.


Next, we showcase an example of the non-blocking send and receive methods
`comm.isend()` and `comm.irecv()`. Non-blocking versions of these
methods allow for the processes involved in transmission/reception of
data to perform other operations in overlap with the communication. In
In contrast, the blocking versions of these methods previously
exemplified do not allow data buffers involved in transmission or
reception of data to be accessed until any ongoing communication
involving the particular processes has been finalized.

```python
!include ../examples/isend_ireceive.py
```

Executing `mpiexec -n 4 python isend_ireceive.py` yields:

```bash
After isend/ireceive, the value in process 2 is None
After isend/ireceive, the value in process 3 is None
After isend/ireceive, the value in process 0 is None
After isend/ireceive, the value in process 1 is 42
```

## Collective Communication

### Broadcast

The `bcast()` method and it is memory version `Bcast()` broadcast a message
from a specified *root* process to all other processes in the communicator
group.

#### Broadcast of a Python Object

In terms of syntax, `bcast()` takes the object to be broadcast and the
parameter `root`, which establishes the rank number of the process broadcasting
the data. If no root parameter is specified, `bcast` will default to
broadcasting from the process with rank 0.

Thus, the two  lines are functionally equivalent.

```python
data = comm.bcast(data, root=0)
data = comm.bcast(data)
```

In our following example, we broadcast a two-entry Python dictionary from a
root process to the rest of the processes in the communicator group.

![Broadcasting data from a root process to the rest of the processes in the communicator group](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/bcast.png){ width=50% }

The following code snippet shows the creation of the dictionary in process with
rank 0. Notice how the variable `data` remains empty in all the other
processes.

``` python
!include ../examples/broadcast.py
```

After running `mpiexec -n 4 python broadcast.py` we get the following:

```
before broadcast, data on rank 3 is: None
before broadcast, data on rank 0 is: 
  {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
before broadcast, data on rank 1 is: None
before broadcast, data on rank 2 is: None
after broadcast, data on rank 3 is: 
  {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
after broadcast, data on rank 0 is: 
  {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
after broadcast, data on rank 1 is: 
  {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
after broadcast, data on rank 2 is: 
  {'size': [1, 3, 8], 'name': ['disk1', 'disk2', 'disk3']}
```

As we can see, all other processes received the data broadcast from the root process.

#### Broadcast of a Memory Object

In our following example, we broadcast a NumPy array from process 0 to the rest
of the processes in the communicator group using the uppercase `comm.Bcast()` method.

``` python
!include ../examples/broadcast_buffer.py
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
 
As we can see, the values in the array at the process with rank 0 have
been broadcast to the rest of the processes in the communicator group.


### Scatter

While bradcast send all data to all processes, scatter send chunks of
data to each process.

In our next example, we will `scatter` the members of a list among the
processes in the communicator group. We illustrate the concept in the
next figure, where we indicate the data that is scattered to the
rnaked processes with $D_i$

![Example to scatter data to different processors from the one with rank 0](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/scatter.png){ width=30% }

#### Scatter Python Objects

The example program executing the sactter is showcased next

``` python
!include ../examples/scatter.py
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

#### Scatter from Python Memory

In the following example, we scatter a NumPy array among the processes in the
communicator group by using the uppercase version of the method `comm.Scatter()`.

``` python
!include ../examples/scatter_buffer.py
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

### Gather

The gather function is the inverse function to scatter. Data from each process is gathered in consecutive order based on the rank of the processor.

#### Gather Python Objects

In this example, data from each process in the communicator group is
gathered in the process with rank 0.

![Example to gather data to different processors from the one with rank 0](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/gather.png){ width=30% }


``` python
!include ../examples/gather.py
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

#### Gather from Python Memory

The example showcases the use of the uppercase method `comm.Gather()`.
NumPy arrays from the processes in the communicator group are gathered
into a 2-D array in process with rank 0.

``` python
!include ../examples/gather_buffer.py
```
       
Executing `mpiexec -n 4 python npgather.py` yields:

```
Buffer in process 2 before gathering:  [2 2 2 2 2 2 2 2 2 2]
Buffer in process 3 before gathering:  [3 3 3 3 3 3 3 3 3 3]
Buffer in process 0 before gathering:  [0 0 0 0 0 0 0 0 0 0]
Buffer in process 1 before gathering:  [1 1 1 1 1 1 1 1 1 1]
recvbuf in process 0 before gathering:
 [[0 0 0 0 0 0 0 0 0 0]
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


### Allgather Memory Objects

This method is a many-to-many communication operation, where data from all processors is gathered in a continuous memory object on each of the processors. This is functionally equivalent to

1. A gather on rank 0
2. A Scatter from rank 0

However, this operation naturally has a performance bottleneck while all communication goes through rank0.
Instead, we can use parallel communication between all of the processes at once to improve the performance.
The optimization is implicit, and the user does not need to worry about it.

We demonstrate its use in the following example. Each process in the
communicator group computes and stores values in a NumPy array
(row). For each process, these values correspond to the multiples of
the process' rank and the integers in the range of the communicator
group's size. After values have been computed in each process, the
different arrays are gathered into a 2D array (table) and distributed
to ALL the members of the communicator group (as opposed to a single
member, which is the case when `comm.Gather()` is used instead).

![Example to gather the data from each process into ALL of the processes in the group](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/allgather.png){ width=30% }

```python
!include ../examples/allgather_buffer.py
```

Executing 

```
$ mpiexec -n 4 python allgather_buffer.py
```

results in the output similar to 

```
Process 1 table before Allgather: [[0. 0.][0. 0.]] 
Process 0 table before Allgather: [[0. 0.][0. 0.]] 
Process 1 table after Allgather:  [[0. 0.][0. 1.]] 
Process 0 table after Allgather:  [[0. 0.][0. 1.]] 
```

As we see, after `comm.Allgather()` is called, every process gets a copy
of the full multiplication table.

We have not provided an example for the Python object version as it is
essentially the same and can easily be developed as an exercise.

## Process Management

### Dynamic Process Management with `spawn`

So far, we have focussed on MPI used on a number of hosts that are
automatically creating the process when mpirun is used.  However, MPI
also offers the ability to sawn a process in a communicator
group. This can be achieved by using a spawn communicator and command.

Using

``` python
MPI.Comm_Self.Spawn
```

will create a child process that can communicate with the parent. 
In the spawn code example, the manager broadcasts an array to the worker.

In this example, we have two python programs, the first one being the
manager and the second being the worker. 

![Example to spawn a program and start it on the different processors from the one with rank 0](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/spawn.png){ width=25% }


``` python
!include ../examples/spawn/manager.py
```

``` python
!include ../examples/spawn/worker.py
```

To execute the example please go to the examples directory and run the manager
program

```
$ cd examples/spawn
$ mpiexec -n 4 python manager.py
```

This will result in:

```
N: 100 rank: 4
N: 100 rank: 1
N: 100 rank: 3
N: 100 rank: 2
Hello
b and rank: 0
c
d
3.1416009869231245
N: 100 rank: 0
N: 100 rank: 1
N: 100 rank: 4
N: 100 rank: 3
N: 100 rank: 2
Hello
b and rank: 0
c
d
3.1416009869231245
N: 100 rank: 0
```

This output depends on which child process is received first. The output can vary.

`WARNING:` When running this program it may not terminate. To
>terminate use for now `CTRL-C`.


### Futures

Futures is an mpi4py module that runs processes in parallel for intercommunication between
such processes. The following Python program creates a visualization of a Julia set by
utilizing this Futures modules, specifically via MPIPoolExecutor.

``` python
!include ../examples/futures/julia-futures.py
```

To run teh program use:

```bash
mpiexec -n 1 python julia-futures.py
```

The number after `-n` can be changed to however many cores are in the computer's processor.
For example, a dual-core processor can use `-n 2` so that more worker processes work to
execute the same program.

The program will output a png image of a Julia set upon successful execution.

You can modify your number of processors accordingly matching your hardware infrastructure.

For example, entering the number `3` will produce a 1920x1440 photo because 640x480 times 3 is 1920x1440. 
Then, the program should output a visualization of a Julia data set as a png image.


# Simple MPI Example Programs

In this section, we will showcase to you some simple MPI example programs.

## GPU Programming with MPI

In case you have access to computers with GPUS you can naturally
utilize them accordingly from Python with the appropriate GPU drivers.

In case not all have a GPU, you can use rankfiles to control the
access and introduce through conditional programming based on rank
access to the GPUs.

# Examples

## MPI Ring Example

The MPI Ring example program is one of the classical programs every
MPI programmer has seen. Here a message is sent from the manager to
the workers while the processors are arranged in a ring, and the last
worker sends the message back to the manager. Instead of just doing
this once, our program does it multiple times and adds every time a
communication is done 1 do the integer send around. Figure 1 showcases
the process graph of this application.

![Processes organized in a ring perform a sum operation](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/images/ring.png){ width=60% }

In the example, the user provides an integer that is transmitted from
the process with rank 0, to process with rank 1, and so on until the data
returns to process 0. Each process increments the integer by 1 before
transmitting it to the next one, so the final value received by
process 0 after the ring is complete is the sum of the original
integer plus the number of processes in the communicator group.


``` python
!include ../examples/ring.py
```

Executing the code in the example by entering ```mpiexec -n 2 python
ring.py``` in the terminal will produce the following result:

```bash
Communicator group with 4 processes
Enter an integer to transmit: 6
Process 0 transmitted value 7 to process 1
Process 1 transmitted value 8 to process 2
Process 2 transmitted value 9 to process 3
Process 3 transmitted value 10 to process 0
Final data received in process 0 after ring is completed: 10
````

As we can see, the integer provided to process 0 (6 in this case) was
successively incremented by each process in the communicator group to
return a final value of 10 at the end of the ring.

## Counting Numbers

The following program generates arrays of random numbers each 20 (n)
in length with the highest number possible being 10 (max_number).  It
then uses a function called count() to count the number of 8's in each
data set.  The number of 8's in each list is stored count_data.
Count_data is then summed and printed out as the total number of 8's.

The program allows you to set the program parameters. Note that the
program has on purpose a bug in it as it does not communicate the
values m, max_number, or find with a broadcast from rank 0 to all
workers. Your task is to modify and complete this program. 

``` python
!include ../examples/count/count.py
```

Executing `mpiexec -n 4 python count.py` gives us:

```
1 1 [7, 5, 2, 1, 5, 5, 5, 4, 5, 2, 6, 5, 2, 1, 8, 7, 10, 9, 5, 6]
3 3 [9, 2, 9, 8, 2, 7, 7, 2, 10, 1, 2, 5, 3, 5, 10, 8, 10, 10, 8, 10]
2 3 [1, 3, 8, 5, 7, 8, 4, 2, 8, 5, 10, 7, 10, 1, 6, 5, 9, 6, 6, 7]
0 3 [6, 9, 10, 2, 4, 8, 8, 9, 4, 1, 6, 8, 6, 9, 7, 5, 5, 6, 3, 4]

0 [3, 1, 3, 3]

Total number of 8's: 10
```

## Monte Carlo Calculation of Pi

A very nice example to showcase the potential for doing lots of
parallel calculations is to calculate the number pi. This is quite
easily achieved while using a monte Carlo method.

We start with the mathematical formulation of the Monte Carlo
calculation of pi. For each quadrant of the unit square, the area is
pi. Therefore, the ratio of the area outside of the circle is pi over
four. With this in mind, we can use the Monte Carlo Method for the
calculation of pi.

The following is a visualization of the program's methodology to calculate pi:

![montecarlographic](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/chapters/images/monte-carlo-visualization.png){ width=50% }

The following montecarlo.py program generates an estimation of pi using the methodology and
equation shown above. Increasing the total number of iterations will increase the accuracy.

``` python
!include ../examples/monte-carlo/montecarlo.py
```

Instead of running this on one processor, we can run the calculation on
many. Implicitly this increases the accuracy while running more
trials at the same time as we run them all in parallel. Overhead does
exist by starting the MPI program and gathering the result. However,
if the trial number is large enough, it is negligible.

The following program shows the MPI implementation:

---

``` python
!include ../examples/monte-carlo/parallel_pi.py
 ```
---

To run this program using git bash, change directory to the folder
containing this program and issue the command:

```bash
$ mpiexec -n 4 python parallel_pi.py
```

The number after `-n` can be changed to however many cores one has on their processor.


Note: Please be advised that we use Cloudmesh.StopWatch which is a 
convenient program to measure time and display the details for the computer. 
However, it is not threadsafe and, at this time, only measures times in the second range. 
If your calculations for other programs are faster or the trial number is too slow, you can use other benchmarking methods.

## Computing a Visualization of Julia Set

The following program outputs a png image of a Julia set. This can be executed with the aforementioned mpiexec command in git bash;
just remember to alter the command to run julia-numba.py after changing the working directory to the same one that julia-numba.py
resides in.

``` python
!include ../examples/futures/julia-numba.py
```


|         |   No Jit (1280x960)  |  Jit Enabled (1280x960) | No Jit (1920x1440) | Jit Enabled (1920x1440) |
|---------|------------|---------------|-------------|------------|
| 1 Core  | 44.898 s   | 45.800 s      |   68.489 s           |   68.610 s |
| 2 Cores | 45.578 s   | 45.714 s      |   67.718 s           |   69.326 s |
| 3 Cores | 43.026 s   | 44.521 s      |   68.785 s           |   69.487 s |
| 4 Cores | 44.746 s   | 44.552 s      |   73.606 s           |   70.257 s |
| 5 Cores | 43.223 s   | 42.825 s      |   68.226 s           |   68.443 s |
| 6 Cores | 45.134 s   | 44.402 s      |   68.437 s           |   67.637 s |

* These benchmark times were generated using a Ryzen 5 3600 CPU with
  16 GB RAM on a Windows 10 computer.

The improvement in shorter runtime with jit is not apparent likely
because the computations required to run this program are not very
complex; the same reason applies to why the increase in cores does not
improve runtime.

However, this example showcases how to run examples with a
parameter to explore the behavior on multiple cores. Naturally, you can
use and explore other parameters once added to the program.


### Assignments

1. Use numba to speed up the code. Create a tutporial including instalation instructions.
2. Display results with matplotlib as created by the picture
3. Modify cloudmesh.Stopwatch so we can use it for smaller time measurments


## Other MPI Example Programs

You will find lots of example programs on the internet when you search for it.
Please let us know about such examples and we will add the here. You can also contribute to our repository and add example programs that we then include in this document. In return you will become a co-author or get acknowledged.

* A program to calculate PI is provided at

  * <https://cvw.cac.cornell.edu/python/exercise>
  * <https://github.com/cloudmesh/cloudmesh-mpi/projects/1?card_filter_query=monte>

* A program to calculate k-means is provided at

  * <https://medium.com/@hyeamykim/parallel-k-means-from-scratch-2b297466fdcd>

# Parameter Management

Although this next topic is not directly related to MPI and mpi4py, it
is very useful in general. Often we ask ourselves the question, how do
we pass parameters to a program, includding MPI. There are multiple
ways to achieve this. With environment variables, command-line
arguments, and configuration files. We will explain each of these
methods and provide simple example.


## Using the Shell Variables to Pass Parameters

`os.environ` in Python allows us to easily access environment
variables that are defined in a shell.  It returns a dictionary having
user’s environmental variable as key and their values as value.

To demonstrate its use, we have written a 
`count.py` program that uses `os.environ` 
to optionally pass parameters to an MPI program.

This example is included in a previous Section `Counting Numbers` and we like you to look it over.

If the user changed the value of N, MAX, or FIND in the
terminal using, for example, `export FIND="5"` (shown below)
os.environ.get("FIND") would set the find variable equal
to 5.

```
$ export FIND="5"
$ mpiexec -n 4 python count.py
1 0 [9, 6, 8, 3, 4, 8, 5, 6, 6, 3, 5, 6, 10, 5, 5, 1, 1, 2, 1, 3]
3 0 [3, 7, 2, 8, 4, 6, 5, 7, 4, 4, 7, 6, 1, 7, 10, 2, 1, 9, 2, 8]
2 0 [10, 8, 10, 8, 7, 2, 2, 7, 4, 3, 3, 7, 10, 8, 1, 5, 1, 4, 6, 5]
0 0 [5, 8, 9, 1, 2, 7, 1, 5, 5, 6, 3, 6, 10, 9, 7, 10, 5, 3, 6, 5]
0 [0, 0, 0, 0]
Total number of 5's: 0
```

However, if the user does not define any environment
variables find will default to 8.

```
$ mpiexec -n 4 python count.py
1 0 [5, 5, 2, 6, 6, 3, 5, 3, 3, 2, 3, 9, 7, 1, 3, 7, 1, 7, 1, 3]
3 1 [7, 1, 5, 1, 2, 2, 10, 7, 2, 1, 2, 6, 4, 6, 10, 10, 5, 8, 10, 10]
2 0 [5, 1, 4, 4, 9, 9, 5, 1, 1, 3, 9, 3, 5, 2, 5, 7, 9, 7, 10, 5]
0 1 [6, 6, 5, 6, 4, 10, 3, 5, 5, 2, 5, 2, 7, 6, 7, 8, 5, 7, 6, 4]
0 [1, 0, 0, 1]
Total number of 8's: 2
```


Assignment:

1. One thing we did not do is use the broadcast method to properly communicate the 3 environment variables. We like you to improve the
   code and submit to us.

Setting the parameter can either be done vi the export shell command such as

```bash
$ export N=8
```

or while passing the parameter in the same line as a command such as demonstrated next

```bash
$ N=1; python environment-parameter.py
```

This can be generalized while using a file with many different parameters and commands. For example, placing this in a file called `run.sh`

```python
$ N=1; python environment-parameter.py
$ N=2; python environment-parameter.py
```


It allows us to execute the programs sequentially in the file with

```bash
$ sh run.sh
```

Let us assume we use the python program

``` python
!include ../examples/parameters/environment-parameter.py
```

This Python program does not set a variable N on its own. It refers to os.environ
which should have previously set N as shown in the beginning of this document's
git bash log. The program does the same procedures as the
previous program once N is set and passed from os.environ.


We are using, in our case also the cloudmesh.StopWatch to allow us easily to fgrep for the results we may be interested in to conduct benchmarks. Here is an example workflow to achieve this

```
# This command creates an environment variable called N
$ export N=10
# This command prints the environment variable called N
$ echo $N
# This command launches a Python environment
$ python -i
>>> import os
>>> os.environ["N"]
>>> exit()
$ python environment-parameter.py
$ sh run.sh
$ sh run.sh | fgrep "csv,processors"
```


### Using click to pass parameters

Click is a convenient mechanism to define parameters that can be passed via options to python programs. To showcase its use please inspect the following program

``` python
!include ../examples/parameters/click-parameter.py
```


You can manually set the variable in git bash in the same line as you open the .py file

```bash
$ python click-parameter.py --n=3
```


## Resources

Here are a couple of links that may be useful. We have not yet looked over them but include them.

* <https://research.computing.yale.edu/sites/default/files/files/mpi4py.pdf>
* <https://www.nesi.org.nz/sites/default/files/mpi-in-python.pdf>
* <https://www.kth.se/blogs/pdc/2019/08/parallel-programming-in-python-mpi4py-part-1/>
* <http://education.molssi.org/parallel-programming/03-distributed-examples-mpi4py/index.html>
* <http://www.ceci-hpc.be/assets/training/mpi4py.pdf>
* <https://www.csc.fi/documents/200270/224366/mpi4py.pdf/825c582a-9d6d-4d18-a4ad-6cb6c43fefd8>

### Assignment

1. Review the resources and provide a short summary that we add to this document above the appropriate link


# Appendix


!include chapters/gitbash.md

## Make on Windows

Makefiles provide a good feature to organize workflows while assembling
programs or documents to create an integrated document. Within `makefiles` you
can define targets that you can call and are then executed. Preconditions can
be used to execute rules conditionally. This mechanism can easily be used to
define complex workflows that require a multitude of interdependent actions to
be performed. Makefiles are executed by the program `make` that is available on
all platforms.

On Linux, it is likely to be pre-installed, while on macOS you can install it
with Xcode. On Windows, you have to install it explicitly. We recommend that
you install `gitbash` first. After you install `gitbash`, you can install
`make` from an administrative `gitbash` terminal window. To start one, go to
the search field next to the Windows icon on the bottom left and type in
gitbash without a `RETURN`. You will then see a selection window that includes
`Run as administrator`. Click on it. As you run it as administrator, it will
allow you to install `make`. The following instructions will provide you with a
guide to install make under windows.

### Installation

Please visit

* <https://sourceforge.net/projects/ezwinports/files/>

and download the file 

* ['make-4.3-without-guile-w32-bin.zip'](https://sourceforge.net/projects/ezwinports/files/make-4.3-without-guile-w32-bin.zip/download)

After the download, you have to extract and unzip the file as follows in a
gitbash that you started as an administrative user:

![administrativegitbash](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/chapters/images/gitbashadmin.png){ width=25% }

Figure: Screenshot of opening gitbash in admin shell 

```bash
$ cp make-4.3-without-guile-w32-bin.zip /usr
$ cd /usr
$ unzip make-4.3-without-guile-w32-bin.zip
```

Now start a new terminal (a regular non-administrative one) and type the
command

```bash
$ which make
```

It will provide you the location if the installation was successful

```bash
/usr/bin/make
```

to make sure it is properly installed and in the correct directory.

## Installing WSL on Windows 10

WSL is a layer that allows the running of Linux executables on a Windows machine. 

To install WSL2 your computer must have Hyper-V support enabled.
This does not work on Windows Home, and you need to upgrade to Windows
Pro, Edu, or some other Windows 10 version that supports it. Windows
Edu is typically free for educational institutions. The Hyper-V must
be enabled from your BIOS, and you need to change your settings if it
is not enabled.

More information about WSL is provided at

* <https://docs.microsoft.com/en-us/windows/wsl/install-win10>

To install WSL2, you can follow these steps while using
Powershell as an administrative user and run

```
ps$ dism.exe /online /enable-feature /featurename:Microsoft-Hyper-V-All /all /norestart
ps$ dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
ps$ dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

The next command will restart your computer so make sure that all your files and applications are saved:
```
ps$ Restart-Computer
```

Windows will say that it is working on updates (enabling the features).
Once logging back in and restarting an elevated Powershell as admin, run:
```
ps$ $url = "https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi"
ps$ $outpath = "$Home\Downloads\wsl_update_x64.msi"
ps$ Invoke-WebRequest -Uri $url -Outfile $outpath
ps$ cd $Home\Downloads
ps$ .\wsl_update_x64.msi
```

Proceed with the installation on screen. Then run:

```
ps$ wsl --set-default-version 2
```

Then download and install the Ubuntu 20.04 LTS image from the Microsoft store:
* <https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab>
and click Launch.

Run Ubuntu and create a username and passphrase.

Make sure not just to give an empty passphrase but choose a secure one.

Next run in a new instance of elevated (admin) Powershell:
```
ps$ wsl.exe --set-version Ubuntu 2
```

Now you can use the Ubuntu distro freely. The WSL2 application will be in your shortcut menu in `Start`. 

!include chapters/benchmark.md

# Assignments

1. Develop a section explaining  what MPI-IO is
2. Develop a section to explain Collective I/O with NumPy arrays.
3. Add a section on how to use Numpy with MPI, including the installation of NumPy. This is not to have a tutorial about numpy,
   but how to use numpy within mpi4py. Subtasks include

  1. Download Numpy with `pip install numpy` in a terminal
  2. `import numpy as np` to use NumPy in the program
  3. Explain the advantages of NumPy over pickled lists
     - Numpy stores memory contiguously
     - Uses a smaller number of bytes 
     - Can multiply arrays by index
     - It is faster
     - Can store different data types, including images
     - Contains random number generators

4. Add a specific, very small tutorial on using some basic numpy features as they may be useful for MPI application
   development. This may include the following and be added to the
   appendix

   1. To define an array type: `np.nameofarray([1,2,3])`
   2. To get the dimension of the array: `nameofarray.ndim`
   3. To get the shape of the array (the number of rows and columns): `nameofarray.shape`
   4. To get the type of the array: `nameofarray.dtype`
   5. To get the number of bytes: `nameofarray.itemsize`
   6. To get the number of elements in the array: `nameofarray.size`
   7. To get the total size: `nameofarray.size * nameofarray.itemsize`

  Please, note that we have a very comprehensive tutorial on NumPy and
  there is no point to repeat that, we may just point to it and
  improve that tutorial where needed instead.

5. Convert the parallel rank program from <https://mpitutorial.com/tutorials/performing-parallel-rank-with-mpi/>
   to mpi4py. Write a tutorial for it.

6. Develop tutorials that showcase multiple communicators and
   groups. See
   <https://mpitutorial.com/tutorials/introduction-to-groups-and-communicators/>

7. Complete the count example while adding a broadcast to it to communicate the parameters. Provide a modified tutorial.

8. Test out the machinefile, host, and rankfile section. Improve if needed.



# Acknowledgements

We like to thank Erin Seliger and Agness Lungua for their effort on
our very early draft of this paper.



# References

[^MPICH]: Reference missing

[^OPENMPI]: Reference missing

[^MISSINGMPI]: References missing
