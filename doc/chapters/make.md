# Make on Windows

Makefiles provide a good feature to organize workflows while assembling
programs or documents to create an integrated document. Within `makefiles` you
can define targets that you can call and are then executed. Preconditions can
be used to execute rules conditionally. This mechanism can easily be used to
define complex workflows that require a multitude of interdependent actions to
be performed. Makefiles are executed by the program `make` that is available on
all platforms.

On Linux, it is likely to be pre-installed, while on macOS you can install it
with Xcode. On Windows, you have to install it explicitly. We recommend that
you install `gitbash` first. After you install `gitbash`, you can install
`make` from an administrative `gitbash` terminal window. To start one, go to
the search field next to the Windows icon on the bottom left and type in
gitbash without a `RETURN`. You will then see a selection window that includes
`Run as administrator. Click on it. As you run it as administrator, it will
allow you to install `make`. The following instructions will provide you with a
guide to install make under windows.

## Installation

Please visit

* <https://sourceforge.net/projects/ezwinports/files/>

and download the file 

* ['make-4.3-without-guile-w32-bin.zip`](https://sourceforge.net/projects/ezwinports/files/make-4.3-without-guile-w32-bin.zip/download)

After the download, you have to extract and unzip the file as follows in a
gitbash that you started as administrative user:

![administrativegitbash](https://github.com/cloudmesh/cloudmesh-mpi/raw/main/doc/chapters/images/gitbashadmin.png)

figure: screenshot of opening gitbash in admin shell 

> ```bash
> $ cp make-4.3-without-guile-w32-bin.zip /usr
> $ cd /usr
> $ unzip make-4.3-without-guile-w32-bin.zip
> ```

Now start a new terminal (a regular non-administrative one) and type the
command

> ```bash
> $ which make
> ```

It will provide you the location if the installation was successful

> ```bash
> /usr/bin/make
> ```

to make sure it is properly installed and in the correct directory.
