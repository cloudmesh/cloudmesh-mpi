OPTIONS=--filter pandoc-include
USER_ID=$(shell id -u)
GROUP_ID=$(shell id -g)
PWD=$(shell pwd)
PANDOC=docker run --rm --volume "${PWD}:/data" --user ${USER_ID}:${GROUP_ID}

.PHONY: report.md

all: image md pdf clean

md:
	${PANDOC} cloudmesh/pandoc ${OPTIONS} ./chapters/report.md -o tmp-1.md
	${PANDOC} cloudmesh/pandoc ${OPTIONS} tmp-1.md  -o tmp-2.md
	${PANDOC} cloudmesh/pandoc ${OPTIONS} tmp-2.md  -o tmp-3.md
	${PANDOC} cloudmesh/pandoc --number-sections chapters/title.md tmp-3.md -o report.md

pdf:
	${PANDOC} cloudmesh/pandoc -s -t latex -V geometry:margin=1in --number-sections --toc chapters/metadata.yaml tmp-3.md -o report.pdf

shell:
	${PANDOC} -it --entrypoint sh cloudmesh/pandoc:latest

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


pdf-native: 
	pandoc -s -t latex -V geometry:margin=1in --number-sections --toc chapters/metadata.yaml tmp-3.md -o report.pdf

