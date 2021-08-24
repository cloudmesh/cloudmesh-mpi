OPTIONS=--filter pandoc-include --filter pandoc-xnos
USER_ID=$(shell id -u)
GROUP_ID=$(shell id -g)
PWD=$(shell pwd)
PANDOC=docker run --rm --volume "${PWD}/..:/data" --user ${USER_ID}:${GROUP_ID}

MPI=chapters/report-mpi.md ../docs/report-mpi.pdf 
GROUP=chapters/management.md chapters/hardware.md ../docs/report-group.pdf

define banner
	@echo
	@echo "############################################################"
	@echo "# $(1) "
	@echo "############################################################"
endef



.PHONY: clean

all: pdf-mpi pdf-group clean

md-mpi: ${MPI}
	$(call banner, "CREATE MPI MARKDOWN DOCUMENT")
	${PANDOC} cloudmesh/pandoc ${OPTIONS} ./chapters/report-mpi.md -o tmp-1.md
	${PANDOC} cloudmesh/pandoc ${OPTIONS} tmp-1.md -o tmp-2.md
	${PANDOC} cloudmesh/pandoc ${OPTIONS} tmp-2.md -o tmp-3.md
	${PANDOC} cloudmesh/pandoc ${OPTIONS} \
		--number-sections tmp-3.md \
		-o ../docs/report-mpi.md

pdf-mpi: ${MPI} md-mpi
	$(call banner, "CREATE MPI PDF DOCUMENT")
	${PANDOC} cloudmesh/pandoc -s \
		-t latex -V geometry:margin=1in --number-sections \
		--toc chapters/metadata-mpi.yaml tmp-3.md \
		-o ../docs/report-mpi.pdf

md-group: ${GROUP}
	$(call banner, "CREATE GROUP MARKDOWN DOCUMENT")
	${PANDOC} cloudmesh/pandoc ${OPTIONS} ./chapters/report-group.md -o tmp-1.md
	${PANDOC} cloudmesh/pandoc ${OPTIONS} tmp-1.md -o tmp-2.md
	${PANDOC} cloudmesh/pandoc ${OPTIONS} tmp-2.md -o tmp-3.md
	${PANDOC} cloudmesh/pandoc ${OPTIONS} --number-sections ./chapters/title-group.md tmp-3.md -o ../docs/report-group.md

pdf-group: ${GROUP} md-group
	$(call banner, "CREATE GROUP PDF DOCUMENT")
	${PANDOC} cloudmesh/pandoc -s -t latex -V geometry:margin=1in --number-sections --toc chapters/metadata-group.yaml tmp-3.md -o ../docs/report-group.pdf

shell:
	${PANDOC} -it -u root --entrypoint bash cloudmesh/pandoc:latest

image:
	docker build -t cloudmesh/pandoc:latest .

clean:
	@rm -f *.toc *.aux *.log rm tmp-?.md


##### TO GEBERATE NATIVELY

native: md-native pdf-native

md-native:
	pandoc ${OPTIONS} chapters/report-mpi.md -o tmp-1.md
	pandoc ${OPTIONS} tmp-1.md  -o tmp-2.md
	pandoc ${OPTIONS} tmp-2.md  -o tmp-3.md
	pandoc --number-sections chapters/title-mpi.md tmp-3.md -o ../docs/report-mpi.md


pdf-native: md-native
	pandoc -s \
		-t latex -V geometry:margin=1in --number-sections \
		--toc chapters/metadata-mpi.yaml \
		../docs/report-mpi.md -o report-mpi.pdf

