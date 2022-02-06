Begin with Python 3.9.8 on Windows 10 Pro.
Begin from Section 4 in [raspberry burn windows tutorial](https://cloudmesh.github.io/pi/tutorial/raspberry-burn-windows/#4-installing-cloudmesh-and-setup)

I suggest following 4.2 instead of 4.1. I also suggest a change to the documentation, adding `cd ..` immediately before `cd cloudmesh-inventory` in section 4.2.

Continue until you reach Section 5.

In Section 5, instead of doing the first block of code, we do
```bash
cms burn image versions --refresh
cms burn image get latest-lite-legacy
```

Ensure `cms burn info` works by running the command.

Do not use `cms burn raspberry` until doing the following (we assume you have a manager and three workers, if not, change accordingly):

```bash
(ENV3) (admin) you@yourlaptop $ cms inventory add cluster "red,red0[1-3]"
(ENV3) (admin) you@yourlaptop $ cms inventory set "red,red0[1-3]" tag to latest-lite-legacy --inventory="inventory-red.yaml"
```

Then do `cms burn raspberry` as follows, altering to accomodate your own setup where needed:

```bash
(ENV3) (admin) you@yourlaptop $ cms burn raspberry "red,red0[1-3]" --password=myloginpassword --disk=4 --locale=en_US.UTF-8 --timezone="America-New_York" "--ssid='Net Work'" --wifipassword=mywifipassword
```

Remember, like in the example above, when doing `cms burn raspberry` command, do NOT include `--new` parameter! This way, the inventory we just created is not disregarded.

After inserting burned cards into Pis and booting: before attempting to ssh to the Pis, ensure that on the laptop, the ~/.ssh/known_hosts file does not have conflicting entries for past red configurations. We suggest that you remove all preexisting entries that start with "red".

Continue from section 6 after inserting burned cards into Pis, removing old entries in known_hosts (if applicable), and booting.

If you already have a cluster_red_keys file when trying to gather, delete the old one.

Another note: when scattering the keys on windows, it might help to cd to the .ssh folder if you receive a "ERROR The file does not exist" error otherwise.

See the following output which shows why it is necessary to `cd` to .ssh folder.

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

Do section 6.4 on red, the manager Pi, but with the newest development version.
