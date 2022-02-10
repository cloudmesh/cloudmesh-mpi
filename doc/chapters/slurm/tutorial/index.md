---
date: 2022-02-10
title: "DRAFT: Installing SLURM on Pre-configured Pi Cluster"
linkTitle: "DRAFT: SLURM on Pi Cluster"
description: "A comprehensive tutorial to install SLURM on a connected Pi Cluster"
author: Jacques Fleischer [github.com/jpfleischer](https://github.com/jpfleischer), Gregor von Laszewski ([laszewski@gmail.com](mailto:laszewski@gmail.com)) [laszewski.github.io](https://laszewski.github.io)
draft: True
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---

{{< imgproc image Fill "600x300" />}}

{{% pageinfo %}}

In this tutorial, we explain how to run a Python script that automatically installs SLURM on a pre-configured Pi
Cluster. This tutorial assumes that the user has access to all nodes (workers) and that one can log in to each node.

**Learning Objectives**

* Learn how to run a Python script to install SLURM on a Pi Cluster
* Test SLURM on the cluster after burning

**Topics covered**

{{% table_of_contents %}}

{{% /pageinfo %}}

## 1. Introduction

There exists yet no automatic script to install SLURM, an open-source job scheduler and workload manager, on a cluster
of Raspberry Pis. Thus, we have developed a Python script that automatically installs SLURM on any number of worker
nodes.

The script is meant to automate an arduous process of logging in and switching back and forth from manager to worker,
with many commands along the way. The script takes inspiration from preexisting tutorials such as those written by
[Garrett Mills](https://glmdev.medium.com/building-a-raspberry-pi-cluster-784f0df9afbd) [^mills].

We assume that the user has access and can login to all nodes; we also assume that manager has the hostname `red`
and that the workers follow an incremental naming schema, such as `red01`, `red02`, `red03`, `red04`, and so on,
with any number of workers possible.

We enable automation of using SSH to issue commands to multiple Pis at a time through the cloudmesh libraries. Thus,
cloudmesh must be installed on the manager Pi before proceeding.

This script does the following:

* Updates packages on each Pi,
* Installs ntpdate package for time synchronization,
* Configures shared storage for sharing configuration files across the cluster,
* Installs the SLURM workload manager and daemons,
* Dynamically writes config files based on IP addresses and hostnames of the Pis,
* Installs MUNGE authentication service for security.

After SLURM is successfully installed, it can be used as a sophisticated manager for running intensive computations
through MPI (Message Passing Interface) and for forays into artificial intelligence, for example.

## 2. Pre-requisites

* Computer/Laptop with Windows 10, macOS, or Linux
* A manager Pi with hostname `red` and cloudmesh installed (with Python version >= 3.9)
* Any number of worker Pis
* The cluster of manager Pi and worker Pi(s) must be preconfigured with login access to each node; they must also have Internet access

For parts for different Pi cluster configurations, please see  lists please see our links on [piplanet.org](https://cloudmesh.github.io/pi/docs/hardware/parts/)


# References 

[^mills]: Building a Raspberry Pi Cluster, Garrett Mills <https://glmdev.medium.com/building-a-raspberry-pi-cluster-784f0df9afbd>
