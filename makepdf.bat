@echo off
scholdoc test.md -o test.tex -H header.tex --number-sections
xelatex test.tex
test.pdf