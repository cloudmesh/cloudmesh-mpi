Begin with Python 3.9.8 on Windows 10 Pro.
Begin from Section 4 in [raspberry burn windows tutorial](https://cloudmesh.github.io/pi/tutorial/raspberry-burn/#4-installing-cloudmesh-and-setup)

I suggest adding `cd ..` immediately before `cd cloudmesh-inventory` in section 4.2.

In Section 5, instead of doing the first block of code, we do
```
cms burn image versions --refresh
cms burn image get latest-lite-legacy
```

when doing `cms burn raspberry` command, do NOT include `--new` parameter!

When attempting to ssh to the Pis, ensure that on the laptop, the ~/.ssh/known_hosts file does not have conflicting entries for past red configurations.

If you already have a cluster_red_keys file when trying to gather, delete the old one.

Another note: when scattering the keys on windows, it might help to cd to the .ssh folder if you receive a "ERROR The file does not exist" error otherwise.

```
you@yourlaptop MINGW64 ~
$ cms host key gather "red,red0[1-3]" \"~/.ssh/cluster_red_keys\"
host key gather red,red0[1-3] "~/.ssh/cluster_red_keys"
Command ****OUTPUT**** 

output omitted for clarity and security!

Timer: 3.0269s Load: 0.0040s host key gather red,red0[1-3] "~/.ssh/cluster_red_keys"
(ENV39)

you@yourlaptop MINGW64 MINGW64 ~
$ cms host key scatter "red,red0[1-3]" \"~/.ssh/cluster_red_keys\"
host key scatter red,red0[1-3] "~/.ssh/cluster_red_keys"
ERROR: The file does not exist
Timer: 0.0080s Load: 0.0040s host key scatter red,red0[1-3] "~/.ssh/cluster_red_keys"
(ENV39)
you@yourlaptop MINGW64 MINGW64 ~
(ENV39)
you@yourlaptop MINGW64 MINGW64 ~
$ cd .ssh
(ENV39)
you@yourlaptop MINGW64 MINGW64 ~/.ssh
$ cms host key scatter "red,red0[1-3]" cluster_red_keys
host key scatter red,red0[1-3] cluster_red_keys
+-------+---------+--------+
| host  | success | stdout |
+-------+---------+--------+
| red   | True    |        |
| red01 | True    |        |
| red02 | True    |        |
| red03 | True    |        |
+-------+---------+--------+
Timer: 4.0332s Load: 0.0040s host key scatter red,red0[1-3] cluster_red_keys
(ENV39)
```
