# FROM ubuntu:21.04
FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

# Install bash
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y wget


# Install LaTeX

RUN apt-get -y install texlive
RUN ln -snf /usr/share/zoneinfo/Etc/UTC /etc/localtime \
    && echo "Etc/UTC" > /etc/timezone

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install texlive-latex-extra
RUN apt-get -y install texlive-fonts-recommended texlive-fonts-extra
RUN unset DEBIAN_FRONTEND
RUN apt-get -y install biber



# Install pandoc-include

RUN wget https://github.com/jgm/pandoc/releases/download/2.14.0.1/pandoc-2.14.0.1-1-amd64.deb
RUN dpkg -i ./pandoc-2.14.0.1-1-amd64.deb

RUN apt install -y python3
RUN apt install -y python3.9-venv
RUN apt install -y python3-pip

# RUN python3 -m venv /ENV3
# CMD ["source /ENV3/bin/activate"]

RUN pip3 install pandoc-include
RUN pip3 install pandoc-xnos

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