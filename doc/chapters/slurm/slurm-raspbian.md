We have attempted to install slurm on Raspbian OS 10 (codename buster).
However, we encounter some issues possibly due to vague instructions in tutorial but we will troubleshoot this.

The tutorial we follow can be found at <https://blog.llandsmeer.com/tech/2020/03/02/slurm-single-instance.html>

All of these commands execute successfully

`$ sudo apt install munge`

```
$ munge -n | unmunge
STATUS:           Success (0)
[...]
```

```
$ sudo apt install mariadb-server
$ sudo mysql -u root
create database slurm_acct_db;
create user 'slurm'@'localhost';
set password for 'slurm'@'localhost' = password('slurmdbpass');
grant usage on *.* to 'slurm'@'localhost';
grant all privileges on slurm_acct_db.* to 'slurm'@'localhost';
flush privileges;
exit
```

`$ sudo apt install slurmd slurm-client slurmctld`

Now we encounter some difficulties.

This configurator <https://slurm.schedmd.com/configurator.html> is meant for latest version of slurm, however we have just installed an earlier
version of slurm. We know that we have installed an earlier version of slurm because `dpkg -l | grep slurm` gives us 18.08.5.2-1+deb10u2

We try to use the configurator meant for latest version of slurm anyways. cluster is set as Cluster Name, red is set as SlurmctldHost, and red is set as NodeName
as per tutorial instructions. Process ID Logging section must be filled out first by issuing command `cat /lib/systemd/system/slurmd.service` to know where PIDFile
is. We find it is in

/run/slurmd.pid

So we enter for SlurmctldPidFile `/run/slurmctld.pid` and for SlurmdPidFile `/run/slurmd.pid`

We hit submit at bottom of form, select all, and then copy. Issue command `sudo nano /etc/slurm-llnl/slurm.conf` and paste the copied text and save file.
REMEMBER if you need to delete everything if something is already within this file, set cursor to beginning of document and set Mark by Command + Shift + 6 
then scroll to bottom and press Ctrl + K (you should now recopy the text that the configurator produced and now shift + insert into nano to paste it.
Then save this file slurm.conf)
