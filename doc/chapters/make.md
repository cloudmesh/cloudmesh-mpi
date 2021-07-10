# Make on Windows

Make fires provide a good feature to organize workflow while
assembling programs or documents to create an integrated document.
Within makefiles defined targets that you can call and are executed.
Through its mechanism, it can easily deal with complex workflows that
require a multitude of actions to be executed. Makefiles are executed
by the program make that is available on all platforms.

On machines such as on machines that run Linux, it is likely to be
pre-installed while on MacOS you can install it with Xcode. On
Windows, you have to explicitly install it and we recommend that you
use get bashed the window so that you can call make from us and get
bash. The following instructions will provide you with a guide to install
make under windows.

## Installation

Please visit

* <https://sourceforge.net/projects/ezwinports/files/>

and download the file 

* ['make-4.3-without-guile-w32-bin.zip`](https://sourceforge.net/projects/ezwinports/files/make-4.3-without-guile-w32-bin.zip/download)

After the download you have to extract and unzip the file as follows in a gitbash that you started as administartive user:

> ```bash
> $ cp make-4.3-without-guile-w32-bin.zip /usr
> $ cd /usr
> $ unzip make-4.3-without-guile-w32-bin.zip
> ```

Now start a new terminal and type the command

> ```bash
> $ which make
> ```

It will provide you the location if the installation was successful

> ```bash
> /usr/bin/make
> ```

to make sure it is properly installed and in the correct directory.
>
