OPTIONS=--from markdown --to markdown --filter pandoc-include
PANDOC=docker run --rm --volume "`pwd`:/data" --user `id -u`:`id -g` # pandoc/latex:2.6

.PHONY: report.md

all:
	pandoc ${OPTIONS} -o tmp-1.md chapters/report.md 
	pandoc ${OPTIONS} -o report.md tmp-1.md 
	rm tmp-1.md

docker:
	${PANDOC} -o tmp-1.md chapters/report.md
	${PANDOC} -o report.md tmp-1.md

image:
	docker build --label=pandoc --tag=pandoc .

