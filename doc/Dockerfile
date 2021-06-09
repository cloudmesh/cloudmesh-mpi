# Base #########################################################################
FROM ubuntu:focal AS ubuntu-builder-base
WORKDIR /app

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -q --no-allow-insecure-repositories update \
  && apt-get install --assume-yes --no-install-recommends \
       software-properties-common \
  && add-apt-repository ppa:hvr/ghc \
  && apt-get install --assume-yes --no-install-recommends \
       ghc-8.8.3=8.8.3-* \
       cabal-install-3.2=3.2* \
       build-essential=12.8* \
       ca-certificates=* \
       curl=* \
       fakeroot=* \
       git \
       libgmp-dev=2:6.* \
       liblua5.3-dev=5.3.3* \
       pkg-config=0.29.1* \
       zlib1g-dev=1:1.2.11.* \
  && rm -rf /var/lib/apt/lists/* \
  && ln -s /opt/ghc/bin/ghc-8.8.3 /usr/bin/ghc \
  && ln -s /opt/cabal/bin/cabal-3.2 /usr/bin/cabal

COPY cabal.root.config /root/.cabal/config
RUN cabal --version \
  && ghc --version \
  && cabal new-update

# Builder ######################################################################
FROM ubuntu-builder-base as ubuntu-builder
ARG pandoc_commit=master
RUN git clone --branch=$pandoc_commit --depth=1 --quiet \
  https://github.com/jgm/pandoc /usr/src/pandoc

COPY ./ubuntu/freeze/pandoc-$pandoc_commit.project.freeze \
     /usr/src/pandoc/cabal.project.freeze

# Copy placeholder for pandoc-citeproc. This might be overwritten with a
# proper binary later.
COPY ./common/placeholder-pandoc-citeproc.sh \
     /usr/local/bin/pandoc-citeproc

# Install Haskell dependencies
WORKDIR /usr/src/pandoc
# Add pandoc-crossref to project
ARG without_crossref=
ARG extra_packages="pandoc-citeproc pandoc-crossref"
RUN test -n "$without_crossref" || \
    printf "extra-packages: pandoc-crossref\n" > cabal.project.local;

RUN cabal new-update \
  && cabal new-build \
      --disable-tests \
      --jobs \
      . $extra_packages

# Cabal's exec stripping doesn't seem to work reliably, let's do it here.
RUN find dist-newstyle \
         -name 'pandoc*' -type f -perm -u+x \
         -exec strip '{}' ';' \
         -exec cp '{}' /usr/local/bin/ ';'

# Core #########################################################################
FROM ubuntu:focal AS ubuntu-core
ARG pandoc_version=edge
LABEL maintainer='Albert Krewinkel <albert+pandoc@zeitkraut.de>'
LABEL org.pandoc.maintainer='Albert Krewinkel <albert+pandoc@zeitkraut.de>'
LABEL org.pandoc.author "John MacFarlane"
LABEL org.pandoc.version "$pandoc_version"

WORKDIR /data
ENTRYPOINT ["/usr/local/bin/pandoc"]

COPY --from=ubuntu-builder \
  /usr/local/bin/pandoc \
  /usr/local/bin/pandoc-citeproc \
  /usr/local/bin/

# Reinstall any system packages required for runtime.
RUN apt-get -q --no-allow-insecure-repositories update \
  && DEBIAN_FRONTEND=noninteractive \
     apt-get install --assume-yes --no-install-recommends \
       ca-certificates=* \
       liblua5.3-0=5.3.3* \
       lua-lpeg=1.0.* \
       libatomic1=10* \
       libgmp10=2:6.* \
       libpcre3=2:8.39-* \
       libyaml-0-2=0.2.* \
       zlib1g=1:1.2.11.* \
  && rm -rf /var/lib/apt/lists/*

# Crossref #####################################################################
FROM ubuntu-core AS ubuntu-crossref
COPY --from=ubuntu-builder \
  /usr/local/bin/pandoc-crossref \
  /usr/local/bin/



#
# UBUNTU 19.10
#
FROM ubuntu:19.10

MAINTAINER Gregor von Laszewski <laszewski@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

#
# UPDATE THE SYSTEM
#
RUN apt-get -y update --fix-missing
RUN apt-get -y dist-upgrade
RUN apt-get install -y --no-install-recommends apt-utils

#
# DEVELOPMENT TOOLS
#
RUN apt-get install -y build-essential checkinstall --fix-missing
RUN apt-get install -y lsb-core
RUN apt-get install -y dnsutils
RUN apt-get install -y libssl-dev
RUN apt-get install -y libffi-dev
RUN apt-get install -y libreadline-gplv2-dev
RUN apt-get install -y libncursesw5-dev
RUN apt-get install -y libsqlite3-dev
RUN apt-get install -y libgdbm-dev
RUN apt-get install -y libc6-dev
RUN apt-get install -y libbz2-dev
RUN apt-get install -y libffi-dev
RUN apt-get install -y zlib1g-dev

RUN apt-get install -y git-core
RUN apt-get install -y git

RUN apt-get install -y wget
RUN apt-get install -y curl
RUN apt-get install -y rsync

RUN apt-get install -y graphviz


#
# install
#
RUN apt-get install -y emacs-nox
RUN apt-get -y install biber

#RUN yes | pacman -Sy biber
#RUN yes | pacman -Sy emacs
#RUN yes | pacman -Sy lsb-release



#
# INSTALL PYTHON 3.8 FROM SOURCE
#

WORKDIR /usr/src

RUN wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
RUN tar xzf Python-3.8.2.tgz

WORKDIR /usr/src/Python-3.8.2

RUN ./configure --enable-optimizations

RUN make altinstall


#
# INSTALL PACKAGED PYTHON 3.8
#

#RUN apt-get install -y software-properties-common
#RUN add-apt-repository ppa:ubuntu-toolchain-r/ppa
# RUN pip install --upgrade pip setuptools

#RUN apt-get autoremove

#RUN apt-get install -y python3.8
# RUN apt-get install python3-distutils
# RUN apt-get install python3-setuptools
# RUN sudo easy_install3 pip
#RUN apt-get install -y python3-pip
#RUN pip3 install --upgrade pip setuptools


RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.8 10
RUN update-alternatives --config python

RUN update-alternatives --install /usr/bin/pip pip /usr/local/bin/pip3.8 10
RUN update-alternatives --config pip

RUN yes '' | update-alternatives --force --all


ENV PATH="/usr/local/bin:${PATH}"

RUN python3.8 --version
RUN python --version
RUN pip install -U pip
RUN pip --version



WORKDIR /usr/local/code

#
# INSTALL PANDOC
#           
RUN wget -q https://github.com/jgm/pandoc/releases/download/2.9.1.1/pandoc-2.9.1.1-1-amd64.deb
RUN dpkg -i pandoc-2.9.1.1-1-amd64.deb
RUN pandoc --version

RUN wget https://github.com/lierdakil/pandoc-crossref/releases/download/v0.3.6.1b/linux-pandoc_2_9_1_1.tar.gz
RUN tar xvf linux-pandoc_2_9_1_1.tar.gz

RUN mv pandoc-crossref /usr/local/bin


RUN git clone https://github.com/cyberaide/bookmanager.git

WORKDIR /usr/local/code/bookmanager


RUN pip install -e .

WORKDIR /root

#ENTRYPOINT ["/bookmanager/bin/pull.sh"]

CMD [ "/bin/bash" ]



