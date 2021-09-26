# Horovod

## Installation

Up-to-date installation instructions may be found at the Horovod Installation Guide [^ref1] section in the official Horovod docs.

In general, installing Horovod will require:
- Python 3.6+
- CMake
- Tensorflow, PyTorch, or MXNet
- OpenMPI or Gloo

then horovod should be able to be installed with pip:
```
$ pip install horovod
```
or with ensuring specific framework dependencies: 

```
$ pip install horovod[keras,tensorflow] // for example
```
or with all frameworks:
```
$ pip install horovod[all-dependencies]
```

For installation details on a per-setup basis, however, be sure to refer to the official guide [^ref1].

## Introduction

Horovod [^ref2] is a framework for distributed deep learning training developed by engineers at Uber. It makes use of a simple infrastructure setup that can be applied easily to any of its supported deep learning frameworks, including TensorFlow, Keras, PyTorch, and MXNet. By elegantly distributing data-parallel training across all of the connected machines and GPUs, it is able to achieve up to 90% scaling efficiency [^ref3].

## Details

The following are a collection of details regarding Horovod that may be of interest to our purposes.

1) Horovod is based on the MPI model.
"Horovod core principles are based on the MPI concepts size, rank, local rank, allreduce, allgather, and broadcast [^ref4]." This allows a single training script to be scaled to any number of GPUs or hosts.
2) Horovod can be used with either an MPI installation (i.e., OpenMPI) or Gloo, which is an open-source library by Facebook.
OpenMPI seems to be the preferred option, though Gloo is reported to have similar performance results when combined with NCCL [^ref8].
4) Horovod includes support for mpi4py [^ref5].
5) Horovod has advanced techniques built-in for increased performance such as tensor fusion [^ref6] and autotuning [^ref7].
6) Horovod includes support for elastic training, which allows it to scale up and down the number of workers dynamically, allowing the job to continue if some hosts fail [^ref9].

## Usage Example



# Reference

[^ref1]: https://horovod.readthedocs.io/en/stable/install_include.html
[^ref2]: https://horovod.ai/
[^ref3]: https://horovod.readthedocs.io/en/stable/summary_include.html#why-horovod
[^ref4]: https://horovod.readthedocs.io/en/stable/concepts.html
[^ref5]: https://horovod.readthedocs.io/en/stable/summary_include.html#mpi4py
[^ref6]: https://horovod.readthedocs.io/en/stable/tensor-fusion.html
[^ref7]: https://horovod.readthedocs.io/en/stable/autotune.html
[^ref8]: https://developer.nvidia.com/nccl
[^ref9]: https://horovod.readthedocs.io/en/stable/elastic_include.html
