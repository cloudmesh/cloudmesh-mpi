OPTIONS=--filter pandoc-include
PANDOC=docker run --rm --volume "`pwd`:/data" --user `id -u`:`id -g` # pandoc/latex:2.6

.PHONY: report.md

all:md pdf clean

md:
	pandoc ${OPTIONS} chapters/report.md -o tmp-1.md
	pandoc ${OPTIONS} tmp-1.md  -o tmp-2.md
	pandoc ${OPTIONS} tmp-2.md  -o tmp-3.md
	pandoc chapters/title.md tmp-3.md -o report.md

pdf: 
	pandoc -s -t latex -V geometry:margin=1in --toc chapters/metadata.yaml tmp-3.md -o report.pdf

clean:
	@rm -f *.toc *.aux *.log rm tmp-?.md

##### NOT SUPPORTED FROM HERE ON


docker:
	${PANDOC} -o tmp-1.md chapters/report.md
	${PANDOC} -o report.md tmp-1.md

image:
	docker build --label=pandoc --tag=pandoc .

#pdf:
#	docker run --rm --volume "`pwd`:/data" --user `id -u`:`id -g` pandoc/latex report.md -o report.pdf
