
# UBUNTU 20.04
#
FROM ubuntu:20.04
MAINTAINER Gregor von Laszewski <laszewski@gmail.com>


ENV DEBIAN_FRONTEND noninteractive

#
# UPDATE THE SYSTEM
#
RUN apt-get -y update
RUN apt-get -y dist-upgrade
RUN apt-get install -y --no-install-recommends apt-utils

#
# SYSTEM TOOLS
#
RUN apt-get install -y \
    git \
    git-core \
    wget \
    curl \
    rsync \
    emacs-nox

#
# DEVELOPMENT TOOLS
#
RUN apt-get install -y build-essential checkinstall --fix-missing
RUN apt-get install -y \
    lsb-core \
    dnsutils \
    libssl-dev \
    libffi-dev \
    libreadline-gplv2-dev \
    libncursesw5-dev \
    libsqlite3-dev \
    libgdbm-dev \
    libc6-dev \
    libbz2-dev \
    libffi-dev \
    zlib1g-dev

#
# GRAPHICS
#
RUN apt-get install -y graphviz

# Install LaTeX

RUN apt-get -y install texlive
RUN ln -snf /usr/share/zoneinfo/Etc/UTC /etc/localtime \
    && echo "Etc/UTC" > /etc/timezone

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install texlive-latex-extra
RUN apt-get -y install texlive-fonts-recommended texlive-fonts-extra
RUN unset DEBIAN_FRONTEND
RUN apt-get -y install biber

#
# INSTALL PYTHON 3.10 FROM SOURCE
#
WORKDIR /usr/src
ENV PYTHON_VERSION=3.10.4

RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
RUN tar xzf Python-${PYTHON_VERSION}.tgz
WORKDIR /usr/src/Python-${PYTHON_VERSION}
RUN ./configure --enable-optimizations
RUN make -j8 build_all
RUN make -j8 altinstall
RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.10 20
RUN update-alternatives --config python
RUN update-alternatives --install /usr/bin/pip pip /usr/local/bin/pip3.10 20
RUN update-alternatives --config pip
RUN yes '' | update-alternatives --force --all
ENV PATH="/usr/bin:/usr/local/bin:${PATH}"

WORKDIR /usr/local/code

#
# INSTALL PANDOC
#
# https://github.com/jgm/pandoc/releases/download/2.17.1.1/pandoc-2.17.1.1-1-amd64.deb

ENV PANDOC_VERSION=2.17.1.1
RUN wget -q https://github.com/jgm/pandoc/releases/download/${PANDOC_VERSION}/pandoc-${PANDOC_VERSION}-1-amd64.deb
RUN dpkg -i pandoc-${PANDOC_VERSION}-1-amd64.deb
RUN pandoc --version

# https://github.com/lierdakil/pandoc-crossref/releases/download/v0.3.12.2a/pandoc-crossref-Linux.tar.xz
ENV CROSSREF_VERSION=v0.3.12.2a
RUN wget https://github.com/lierdakil/pandoc-crossref/releases/download/${CROSSREF_VERSION}/pandoc-crossref-Linux.tar.xz
RUN tar xvf pandoc-crossref-Linux.tar.xz

RUN mv pandoc-crossref /usr/local/bin

#
# Pandoc extensions
#
RUN pip install pandoc-include
RUN pip install pandoc-xnos

#
# BOOKMANAGER
#
RUN git clone https://github.com/cyberaide/bookmanager.git

WORKDIR /usr/local/code/bookmanager


RUN pip install -e .

#
# CHECK
#
RUN python --version
RUN pip install -U pip
RUN pip --version
RUN pandoc --version

ENTRYPOINT ["pandoc"]

#RUN wget http://mirror.ctan.org/systems/texlive/tlnet/update-tlmgr-latest.sh
#RUN sh update-tlmgr-latest.sh


#RUN apk add texlive-bibtexextra

WORKDIR /data/doc


#RUN tlmgr update --all --self
#RUN tlmgr install tcolorbox
#RUN tlmgr install pgf
#RUN tlmgr install xcolor
#RUN tlmgr install environ
#RUN tlmgr install trimspaces
#RUN tlmgr install mathpazo
#RUN tlmgr install parskip
#RUN tlmgr install adjustbox
#RUN tlmgr install collectbox
#RUN tlmgr install eurosym
#RUN tlmgr install ucs
#RUN tlmgr install enumitem
#RUN tlmgr install jknapltx rsfs
#RUN tlmgr install collection-fontsrecommended
#RUN tlmgr install titling

#RUN apk add make
#RUN apk add git
#RUN apk add ghc
# RUN pip install --upgrade --force --no-cache git+https://github.com/DCsunset/pandoc-include
##RUN apk add cabal
#RUN cabal update
#RUN cabal install pandoc-include-code