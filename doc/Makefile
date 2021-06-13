OPTIONS=--filter pandoc-include
USER_ID=$(shell id -u)
GROUP_ID=$(shell id -g)
PWD=$(shell pwd)
PANDOC=docker run --rm --volume "${PWD}/..:/data" --user ${USER_ID}:${GROUP_ID}

MPI=chapters/preface.md chapters/introduction.md chapters/mpi.md chapters/dl.md ../docs/report-mpi.pdf 
GROUP=chapters/management.md chapters/hardware.md ../docs/report-group.pdf

.PHONY: clean

all: pdf-mpi pdf-group clean

md-mpi: ${MPI}
	${PANDOC} cloudmesh/pandoc ${OPTIONS} ./chapters/report-mpi.md -o tmp-1.md
	${PANDOC} cloudmesh/pandoc ${OPTIONS} tmp-1.md -o tmp-2.md
	${PANDOC} cloudmesh/pandoc ${OPTIONS} tmp-2.md -o tmp-3.md
	${PANDOC} cloudmesh/pandoc --number-sections ./chapters/title-mpi.md tmp-3.md -o ../docs/report-mpi.md

pdf-mpi: ${MPI} md-mpi 
	${PANDOC} cloudmesh/pandoc -s -t latex -V geometry:margin=1in --number-sections --toc chapters/metadata-mpi.yaml tmp-3.md -o ../docs/report-mpi.pdf

md-group: ${GROUP}
	${PANDOC} cloudmesh/pandoc ${OPTIONS} ./chapters/report-group.md -o tmp-1.md
	${PANDOC} cloudmesh/pandoc ${OPTIONS} tmp-1.md -o tmp-2.md
	${PANDOC} cloudmesh/pandoc ${OPTIONS} tmp-2.md -o tmp-3.md
	${PANDOC} cloudmesh/pandoc --number-sections ./chapters/title-group.md tmp-3.md -o ../docs/report-group.md

pdf-group: ${GROUP} md-group
	${PANDOC} cloudmesh/pandoc -s -t latex -V geometry:margin=1in --number-sections --toc chapters/metadata-group.yaml tmp-3.md -o ../docs/report-group.pdf

shell:
	${PANDOC} -it -u root --entrypoint bash cloudmesh/pandoc:latest

image:
	docker build -t cloudmesh/pandoc:latest .

clean:
	@rm -f *.toc *.aux *.log rm tmp-?.md

##### TO GEBERATE NATIVELY

all-native: md-native pdf-native

md-native:
	pandoc ${OPTIONS} chapters/report.md -o tmp-1.md
	pandoc ${OPTIONS} tmp-1.md  -o tmp-2.md
	pandoc ${OPTIONS} tmp-2.md  -o tmp-3.md
	pandoc --number-sections chapters/title.md tmp-3.md -o report.md


pdf-native: md-native
	pandoc -s -t latex -V geometry:margin=1in --number-sections --toc chapters/metadata.yaml tmp-3.md -o report.pdf

