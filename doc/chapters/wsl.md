**Installing WSL on Windows 10**
Visit https://docs.microsoft.com/en-us/windows/wsl/install-win10 for further detail
This is going off the manual installation

Open Powershell as an administrator and run dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
Next, run: dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
Download Ubuntu 20.04 LTS from the Microsoft store.
Run Ubuntu and create a username and passphrase.

In Powershell, run wsl --set-default-version 2. We will be using WSL 2. 

