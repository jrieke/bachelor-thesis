@echo off
scholdoc bachelor-thesis.md -o bachelor-thesis.tex -H header.tex --number-sections
postprocess bachelor-thesis.tex
xelatex bachelor-thesis.tex
bachelor-thesis.pdf