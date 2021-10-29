# Running a benchmark for tensorflow on your system

## Requirements

- Python 3 environment with:
  -  TensorFlow 2.5.0
  -  Cloudmesh

To install Cloudmesh for our purposes, we only need the following commands:

```bash
pip install cloudmesh-installer
cloudmesh-installer get cmd5
```

## Benchmark 1: Basic MNIST

```bash
$ curl -Ls http://cloudmesh.github.io/get/pi/tensorflow/benchmark/mnist | python
```

## Results

Raspberry Pi 4 running Ubuntu 20.04 Server 64-bit

```
+---------------------+------------------------------------------------------------------+
| Attribute           | Value                                                            |
|---------------------+------------------------------------------------------------------|
| BUG_REPORT_URL      | "https://bugs.launchpad.net/ubuntu/"                             |
| DISTRIB_CODENAME    | focal                                                            |
| DISTRIB_DESCRIPTION | "Ubuntu 20.04.3 LTS"                                             |
| DISTRIB_ID          | Ubuntu                                                           |
| DISTRIB_RELEASE     | 20.04                                                            |
| HOME_URL            | "https://www.ubuntu.com/"                                        |
| ID                  | ubuntu                                                           |
| ID_LIKE             | debian                                                           |
| NAME                | "Ubuntu"                                                         |
| PRETTY_NAME         | "Ubuntu 20.04.3 LTS"                                             |
| PRIVACY_POLICY_URL  | "https://www.ubuntu.com/legal/terms-and-policies/privacy-policy" |
| SUPPORT_URL         | "https://help.ubuntu.com/"                                       |
| UBUNTU_CODENAME     | focal                                                            |
| VERSION             | "20.04.3 LTS (Focal Fossa)"                                      |
| VERSION_CODENAME    | focal                                                            |
| VERSION_ID          | "20.04"                                                          |
| cpu                 |                                                                  |
| cpu_cores           | 4                                                                |
| cpu_count           | 4                                                                |
| cpu_threads         | 4                                                                |
| frequency           | scpufreq(current=1100.0, min=600.0, max=1500.0)                  |
| mem.active          | 1.4 GiB                                                          |
| mem.available       | 6.5 GiB                                                          |
| mem.free            | 5.4 GiB                                                          |
| mem.inactive        | 557.8 MiB                                                        |
| mem.percent         | 15.1 %                                                           |
| mem.total           | 7.6 GiB                                                          |
| mem.used            | 1.0 GiB                                                          |
| platform.version    | #49-Ubuntu SMP PREEMPT Wed Sep 29 17:49:16 UTC 2021              |
| python              | 3.8.10 (default, Sep 28 2021, 16:10:42)                          |
|                     | [GCC 9.3.0]                                                      |
| python.pip          | 20.0.2                                                           |
| python.version      | 3.8.10                                                           |
| sys.platform        | linux                                                            |
| uname.machine       | aarch64                                                          |
| uname.node          | ubuntu                                                           |
| uname.processor     | aarch64                                                          |
| uname.release       | 5.4.0-1045-raspi                                                 |
| uname.system        | Linux                                                            |
| uname.version       | #49-Ubuntu SMP PREEMPT Wed Sep 29 17:49:16 UTC 2021              |
| user                | ubuntu                                                           |
+---------------------+------------------------------------------------------------------+

+---------+----------+--------+--------+---------------------+-------+-------+--------+--------+-------+-----------------------------------------------------+
| Name    | Status   |   Time |    Sum | Start               | tag   | msg   | Node   | User   | OS    | Version                                             |
|---------+----------+--------+--------+---------------------+-------+-------+--------+--------+-------+-----------------------------------------------------|
| install | ok       | 64.029 | 64.029 | 2021-10-28 20:03:33 |       |       | ubuntu | ubuntu | Linux | #49-Ubuntu SMP PREEMPT Wed Sep 29 17:49:16 UTC 2021 |
+---------+----------+--------+--------+---------------------+-------+-------+--------+--------+-------+-----------------------------------------------------+

# csv,timer,status,time,sum,start,tag,msg,uname.node,user,uname.system,platform.version
# csv,install,ok,64.029,64.029,2021-10-28 20:03:33,,None,ubuntu,ubuntu,Linux,#49-Ubuntu SMP PREEMPT Wed Sep 29 17:49:16 UTC 2021
```

Henry's Desktop PC (CPU Only)

```
+------------------+--------------------------------------------------------------------------------+
| Attribute        | Value                                                                          |
|------------------+--------------------------------------------------------------------------------|
| cpu              |                                                                                |
| cpu_cores        | 4                                                                              |
| cpu_count        | 8                                                                              |
| cpu_threads      | 8                                                                              |
| frequency        | scpufreq(current=4200.0, min=0.0, max=4200.0)                                  |
| mem.available    | 23.3 GiB                                                                       |
| mem.free         | 23.3 GiB                                                                       |
| mem.percent      | 27.0 %                                                                         |
| mem.total        | 31.9 GiB                                                                       |
| mem.used         | 8.6 GiB                                                                        |
| platform.version | ('10', '10.0.19043', 'SP0', 'Multiprocessor Free')                             |
| python           | 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] |
| python.pip       | 21.2.4                                                                         |
| python.version   | 3.9.7                                                                          |
| sys.platform     | win32                                                                          |
| uname.machine    | AMD64                                                                          |
| uname.node       | Phasma                                                                         |
| uname.processor  | Intel64 Family 6 Model 158 Stepping 9, GenuineIntel                            |
| uname.release    | 10                                                                             |
| uname.system     | Windows                                                                        |
| uname.version    | 10.0.19043                                                                     |
| user             | Henry                                                                          |
+------------------+--------------------------------------------------------------------------------+

+---------+----------+--------+-------+---------------------+-------+-------+--------+--------+---------+----------------------------------------------------+
| Name    | Status   |   Time |   Sum | Start               | tag   | msg   | Node   | User   | OS      | Version                                            |
|---------+----------+--------+-------+---------------------+-------+-------+--------+--------+---------+----------------------------------------------------|
| install | ok       |  7.069 | 7.069 | 2021-10-28 20:08:17 |       |       | Phasma | Henry  | Windows | ('10', '10.0.19043', 'SP0', 'Multiprocessor Free') |
+---------+----------+--------+-------+---------------------+-------+-------+--------+--------+---------+----------------------------------------------------+

# csv,timer,status,time,sum,start,tag,msg,uname.node,user,uname.system,platform.version
# csv,install,ok,7.069,7.069,2021-10-28 20:08:17,,None,Phasma,Henry,Windows,('10', '10.0.19043', 'SP0', 'Multiprocessor Free')
```

