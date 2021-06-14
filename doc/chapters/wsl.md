## Installing WSL on Windows 10

TODO: what is wsl

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

TODO: how to start it the next time
