all:
	pandoc --from markdown --to markdown --filter pandoc-include report-in.md report.md 
