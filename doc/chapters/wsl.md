## Installing WSL on Windows 10

TODO: Cooper, what is wsl

To install WSL2 your computer must have Hyper-V support enabled.
THis doe snot work on Windows HOmew and you need to upgrade to Windows
Pro, Edu or some other Windows 10 version that supports it. Windows
Edu is typically free for educational institutions. The HYper-V must
be enabled from your Bios and you need to change your settings if it
is not enabled.

More information about WSL is provided at

* <https://docs.microsoft.com/en-us/windows/wsl/install-win10> for further detail

To install WSL2 you can follow these directions while using
Powershell as an administrative user and run

```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl --set-default-version 2
```

Next, Download Ubuntu 20.04 LTS from the Microsoft store 

* <https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab>

Run Ubuntu and create a username and passphrase.

Make sur enot to just give an empty passphrase but chose a secure one.

- [ ] TODO: Cooper, how to start it the next time
