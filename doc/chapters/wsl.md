## Installing WSL on Windows 10

WSL is a layer that allows the running of Linux executables on a Windows machine. 

To install WSL2 your computer must have Hyper-V support enabled.
This does not work on Windows Home, and you need to upgrade to Windows
Pro, Edu, or some other Windows 10 version that supports it. Windows
Edu is typically free for educational institutions. The Hyper-V must
be enabled from your Bios, and you need to change your settings if it
is not enabled.

More information about WSL is provided at

* <https://docs.microsoft.com/en-us/windows/wsl/install-win10>

To install WSL2, you can follow these steps while using
Powershell as an administrative user and run

> ```
> ps$ dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
> ps$ dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
> ps$ wsl --set-default-version 2
> ```

Next, Download the Ubuntu 20.04 LTS image from the Microsoft store

* <https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab>

Run Ubuntu and create a username and passphrase.

Make sure not just to give an empty passphrase but chose a secure one.

Next run in Powershell

> ```
> ps$ wsl.exe --set-version Ubuntu20.04 2
> ```

Now you can use the Ubuntu distro freely. The WSL2 application will be in your shortcut menu in `Start`. 
