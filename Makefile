.PHONY: main clean FORCE

main: SeniorThesis.pdf

%.pdf: FORCE
	latexmk -pdflatex='lualatex -interaction nonstopmode --shell-escape' -pdf $(patsubst %.pdf,%.tex,$@)

clean:
	latexmk -pdf -C
