FROM pandoc/latex:latest

# Install bash
RUN apk update
RUN apk upgrade
RUN apk add bash

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# Install pandoc-include

RUN pip install pandoc-include

RUN apk add texmf-dist texlive-full
#RUN apk add texlive-extra
#RUN apk add texlive-bibtexextra
RUN apk add biber


#RUN tlmgr update --all --self
#RUN tlmgr update --all
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
## RUN tlmgr install ecs
#RUN tlmgr install ucs
#RUN tlmgr install enumitem
#RUN tlmgr install ulem
## RUN tlmgr install mathrsfs
#RUN tlmgr install jknapltx rsfs
#RUN tlmgr install collection-fontsrecommended
#RUN tlmgr install titling
