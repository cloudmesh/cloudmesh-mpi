# Horovod

## Introduction

Horovod [^ref2] is a framework for distributed deep learning training
developed by engineers at Uber. It makes use of a simplified
infrastructure setup for training distribution that can be applied to any of the
supported deep learning frameworks, including TensorFlow, Keras,
PyTorch, and MXNet. By distributing data-parallel training across all
of the connected hosts and GPUs, it reportedly achieves up to 90%
scaling efficiency [^ref3].

## MPI vs Gloo
TODO

## Installation

Horovod can be installed on many systems. The web page of Horovod
provides the official Installation Guide [^ref1].

Installing Horovod will require:

* Python 3.6+
* CMake
* Tensorflow, PyTorch, or MXNet
* OpenMPI (optional, could use Gloo, which is included)

We will outline here simple install instructions for various operating
systems while also describing different instalations based on MPI vs Gloo

### Windows with OpenMPI

TODO: NOT TESTED

1. We assume you have gitbash installed. We also assume that you use
   for the installation steps an administrative gitbash terminal

   TBD (see our docuementatio in cloudmesh-mpi)
   no reason to duplicate

2. We assume that you use a virtual env

   TBD (seee description in cloudmesh-mpi or Linux book from gregor)

   No need to replicate this. 

1. Check Python installation to ensure version 3.6+. Update if
   necessary.

   ```bash
   $ which python 
   $ python --version
   ```

2. Install CMake

    Go to https://cmake.org/download/. Under binary distributions,
	download the latest Windows installer.  NOTE: During installation,
	be sure to select the checkbox to modify the PATH variable. If not
	selected, this must be done manually. You can do it directly from
	the commandline with the following commands:

   	```bash
	$ cd ~/Download
	$ wget https://github.com/Kitware/CMake/releases/download/v3.21.3/cmake-3.21.3-windows-x86_64.msi
	$ msiexec /i cmake-3.21.3-windows-x86_64.msi`
	```

	TODO: does this allow setting the path. If not can we do a prg
    that does this?

3. Install OpenMPI

   Follow instructions found at the following link for your specific
   system:
   https://github.com/cloudmesh/cloudmesh-mpi/blob/main/docs/report-mpi.md

5. Install Horovod

   We will install Horovod for OpenMPI with tensorflow. We will set
   environment variables to ensure proper values for the pip
   installation.

   ```
   $ export HOROVOD_WITHOUT_GLOO=1
   $ export HOROVOD_WITH_MPI=1
   $ export HOROVOD_WITH_TENSORFLOW=1
   $ pip install horovod[tensorflow]
   ```

### MacOS with OpenMPI

TODO: NOT TESTED

1. Check Python installation to ensure version 3.6+. Update if
   necessary.

   ```
   $ python --version
   ```

2. Install CMake

   * Go to https://cmake.org/download/. Under binary distributions,
     download the latest MacOS version as either a disk image or tarball.
   * Copy CMake.app into /Applications
   * Add the install directory (e.g. /Applications/CMake.app/Contents/bin) to PATH

3. Install OpenMPI

   The easiset way to install cmake is via homebrew using

   ```bash
   $ brew install cmake
   ```

   Alternatively, follow instructions found at the following link for your specific
   system:
   https://github.com/cloudmesh/cloudmesh-mpi/blob/main/docs/report-mpi.md

4. Install Horovod

   We will install Horovod for OpenMPI with tensorflow. We will set
   environment variables to ensure proper values for the pip
   installation.

   ```bash
   $ pip install tensorflow
   $ export HOROVOD_WITHOUT_GLOO=1
   $ export HOROVOD_WITH_MPI=1
   $ export HOROVOD_WITH_TENSORFLOW=1
   $ pip install "horovod[tensorflow]"
   ```

For Gloo make sure lubuv is installed first

```bash
$ brew install libuv
```

### Linux with OpenMPI

1. Check Python installation to ensure version 3.6+. Update if necessary.
```
$ python --version
```
2. Install CMake

Go to https://cmake.org/download/. Under binary distributions,
download the latest pre-compiled binaries for your platform.  NOTE: If
no binary is available for your platform, you will have to install
from source. See https://cmake.org/install/ under the Linux, UNIX
section for more details.

TODO: apt get instead?

3. Install OpenMPI

Follow instructions found at the following link for your specific
system:
https://github.com/cloudmesh/cloudmesh-mpi/blob/main/docs/report-mpi.md

4. Install Horovod

   We will install Horovod for OpenMPI with tensorflow. We will set
   environment variables to ensure proper values for the pip
   installation.

   ```
   $ export HOROVOD_WITHOUT_GLOO=1
   $ export HOROVOD_WITH_MPI=1
   $ export HOROVOD_WITH_TENSORFLOW=1
   $ pip install horovod[tensorflow]
   ```

## Details

The following are a collection of details regarding Horovod that may
be of interest to our purposes.

1. Horovod is based on the MPI model.  "Horovod core principles are
   based on the MPI concepts size, rank, local rank, allreduce,
   allgather, and broadcast [^ref4]." This allows a single training
   script to be scaled to any number of GPUs or hosts.
2. Horovod can be used with either an MPI installation (i.e., OpenMPI)
   or Gloo, which is an open-source library by Facebook.  OpenMPI
   seems to be the preferred option, though Gloo is reported to have
   similar performance results when combined with NCCL [^ref8]
   [^ref1].
4. Horovod includes support for mpi4py [^ref5].
5. Horovod has techniques built-in for increased performance in the
   distributed training process such as tensor fusion [^ref6] and
   autotuning [^ref7].
6. Horovod includes support for elastic training, which allows it to
   scale up and down the number of workers dynamically, allowing the
   job to continue if some hosts fail [^ref9].

## Example

The following example is a modified version with added commentary of
code from the official horovod GitHub repo [^ref10].  This basic
example uses keras with tensorflow 2.0, but the implementation is
incredibly similar between other supported frameworks. See the
official docs [^ref11] for individual differences in implementation
between each framework.



```python
# Step one: import horovod for the required framework
import tensorflow as tf
import horovod.tensorflow.keras as hvd

# Step two: initialize horovod
hvd.init()

# Step three: pin each GPU to a single process
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
if gpus:
    tf.config.experimental.set_visible_devices(gpus[hvd.local_rank()], 'GPU')

# Step four: import the data, build the model, and scale the learning
# rate to the number of GPUs

# Build model and dataset
dataset = ...
model = ...

# Scale learning rate to # of GPUs
scaled_lr = 0.001 * hvd.size()
opt = tf.optimizers.Adam(scaled_lr)

# Step five: Wrap the optimizer with a Horovod DistributedOptimizer
opt = hvd.DistributedOptimizer(opt)

# Step five: Ensure experimental_run_tf_function=False so that the
# DistributedOptimizer is used, and broadcast to ensure workers are
# initialized consistently

# Horovod: Specify `experimental_run_tf_function=False` to ensure
# TensorFlow uses hvd.DistributedOptimizer() to compute gradients.

mnist_model.compile(loss=tf.losses.SparseCategoricalCrossentropy(),
                    optimizer=opt,
                    metrics=['accuracy'],
                    experimental_run_tf_function=False)

# Horovod: broadcast initial variable states from rank 0 to all other
# processes.  This is necessary to ensure consistent initialization of
# all workers when training is started with random weights or restored
# from a checkpoint.

callbacks = [
    hvd.callbacks.BroadcastGlobalVariablesCallback(0),
]

# Step six: save checkpoints only on worker 0 to prevent corruption
if hvd.rank() == 0:
    callbacks.append(keras.callbacks.ModelCheckpoint('./checkpoint-{epoch}.h5'))

# Step seven: Begin the training
model.fit(dataset,
          steps_per_epoch=500 // hvd.size(),
          callbacks=callbacks,
          epochs=24,
          verbose=1 if hvd.rank() == 0 else 0)
```

## Assignments

1. Develop instruction to install Horovod with Gloo on Windows
2. Develop instruction to install Horovod with Gloo on macOS
2. Develop instruction to install Horovod with Gloo on Ubuntu20.04
3. Develop instruction to install Horovod with Gloo on RaspberyOS
4. Develop instruction to install Horovod with Gloo on Raspbery with
   Ubuntu 20.04
5. Develop instructions on how to create a Ubuntu20.04 OS that is
   hosted on a USB stick or external USB hard drive so you can use
   your laptop as Ubuntu machine
6. Create a tuturial for gitbash.
   * Explain how to change color on
     startup vi prefernces (light background black color)
   * Explain how to copy content from windows/browser into gitbash
     shell
   * explain  how we can set path variables from te shell via a
     commandline so that its preseved when we start a new gitbash
7. In macOS zsh explain how to set a prompt that hat the ENV as prefix

## References

[^ref1]: https://horovod.readthedocs.io/en/stable/install_include.html
[^ref2]: https://horovod.ai/
[^ref3]: https://horovod.readthedocs.io/en/stable/summary_include.html#why-horovod
[^ref4]: https://horovod.readthedocs.io/en/stable/concepts.html
[^ref5]: https://horovod.readthedocs.io/en/stable/summary_include.html#mpi4py
[^ref6]: https://horovod.readthedocs.io/en/stable/tensor-fusion.html
[^ref7]: https://horovod.readthedocs.io/en/stable/autotune.html
[^ref8]: https://developer.nvidia.com/nccl
[^ref9]: https://horovod.readthedocs.io/en/stable/elastic_include.html
[^ref10]: https://github.com/horovod/horovod/blob/master/examples/tensorflow2/tensorflow2_keras_mnist.py
[^ref11]: https://horovod.readthedocs.io/en/stable/summary_include.html
