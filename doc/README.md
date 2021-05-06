# Overview

After reflecting on the meeting I decided that in order to increase your python knowledge and to also lead you towards research we will be developing initially a tutorial that teaches students how to use MPI (Message Passing Interface). We do this with something that is called mpi4py. (later on we will use this to coordinate AI algorithms) We will develop multiple sections to this tutorial and each of you will each week work on a chapter so it can be redone by others. You can also work together and share each others ideas and thoughts openly as well as ask questions. We will do the following structured tasks (you will need to know what plagiarism is and when and how you need to cite):

## Installation of python on your hardware

* Windows 10
* MacOs
* Raspberry (using our cms burn)

Each installation documents the install from python.org

## Introduction to MPI

* What is MPI and why do you want to use it

* What are some example MPI functionalities and usage patterns (send receive, embarrassing parallel

## Hello World

* program to test the infrastructure
* run on single host with n cores
* run on mulitple hosts with each having n cores

## Monte Carlo calculation of Pi

* Mathematical formulation of Monte Carlo
* Example program to run Montecarlo on multiple hosts
* Benchmarking of the code
  * cloudmesh.common (not thread safe, but still can be used, research how to use it in multiple threads)
  * other strategies to benchmark, you research (only if really needed
* Use numba to speed up the code
  * describe how to install
* showcase basic usage on our monte carlo function
* display results with matplotlib

## MPI Functionality examples

* broadcast
* send receive
* gather scatter
* task processing (spwan, pull, …)
* examples for other collective communication methods

## GPU Programming with MPI

Only possibly for someone with GPU (contact me if you do)
Once we are finished with MPI we will use and look at python dask and other frameworks as well as rest services to interface with the mpi programs. This way we will be able to expose the cluster to anyone and they do not even know they use a cluster while exposing this as a single function … (edited) 

The github repo is used by all of you to have write access and contribute to the research effort easily and in parallel.
You will get out of this as much as you put in. Thus it is important to set several dedicated hours  aside (ideally each week)  and contribute your work to others.

It is difficult to asses how long the above task takes as we just get started and we need to learn first how we work together as a team. If I were to do this alone it may take a week, but as you are less experienced it would likely take longer. However to decrease the time needed we can split up work and each of you will work on a dedicated topic (but you can still work in smaller teams if you desire). We will start assigning tasks in github once this is all set up.
