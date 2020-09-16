# You want latexmk to *always* run, because make does not have all the info.
# Also, include non-file targets in .PHONY so they are run regardless of any
# file of the given name existing.
.PHONY: week\ 1/Exercises_week_1.pdf week\ 2/Exercises_week_2.pdf week\ 3/Exercises_week_3.pdf week\ 4/Exercises_week_4.pdf week\ 5/Exercises_week_5.pdf week\ 6/Exercises_week_6.pdf week\ 7/Exercises_week_7.pdf week\ 9/Exercises_week_9.pdf week\ 10/Exercises_week_10.pdf supplementary\ material/using_git.pdf all clean

# The first rule in a Makefile is the one executed by default ("make"). It
# should always be the "all" rule, so that "make" and "make all" are identical.
all: week\ 1/Exercises_week_1.pdf week\ 2/Exercises_week_2.pdf week\ 3/Exercises_week_3.pdf week\ 4/Exercises_week_4.pdf week\ 5/Exercises_week_5.pdf week\ 6/Exercises_week_6.pdf week\ 7/Exercises_week_7.pdf week\ 9/Exercises_week_9.pdf week\ 10/Exercises_week_10.pdf supplementary\ material/using_git.pdf

# CUSTOM BUILD RULES

# In case you didn't know, '$@' is a variable holding the name of the target,
# and '$<' is a variable holding the (first) dependency of a rule.
# "raw2tex" and "dat2tex" are just placeholders for whatever custom steps
# you might have.

%.tex: %.raw
		./raw2tex $< > $@

%.tex: %.dat
		./dat2tex $< > $@

# MAIN LATEXMK RULE

# -pdf tells latexmk to generate PDF directly (instead of DVI).
# -pdflatex="" tells latexmk to call a specific backend with specific options.
# -use-make tells latexmk to call make for generating missing files.

# -interaction=nonstopmode keeps the pdflatex backend from stopping at a
# missing file reference and interactively asking you for an alternative.
week\ 1/Exercises_week_1.pdf: week\ 1/Exercises_week_1.tex
		latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode" -use-make -output-directory=week\ 1/ week\ 1/Exercises_week_1.tex

week\ 2/Exercises_week_2.pdf: week\ 2/Exercises_week_2.tex
		latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode" -use-make -output-directory=week\ 2/ week\ 2/Exercises_week_2.tex

week\ 3/Exercises_week_3.pdf: week\ 3/Exercises_week_3.tex
		latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode" -use-make -output-directory=week\ 3/ week\ 3/Exercises_week_3.tex

week\ 4/Exercises_week_4.pdf: week\ 4/Exercises_week_4.tex
		latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode" -use-make -output-directory=week\ 4/ week\ 4/Exercises_week_4.tex

week\ 5/Exercises_week_5.pdf: week\ 5/Exercises_week_5.tex
		latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode" -use-make -output-directory=week\ 5/ week\ 5/Exercises_week_5.tex

week\ 6/Exercises_week_6.pdf: week\ 6/Exercises_week_6.tex
		latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode" -use-make -output-directory=week\ 6/ week\ 6/Exercises_week_6.tex

week\ 7/Exercises_week_7.pdf: week\ 7/Exercises_week_7.tex
		latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode" -use-make -output-directory=week\ 7/ week\ 7/Exercises_week_7.tex

week\ 9/Exercises_week_9.pdf: week\ 9/Exercises_week_9.tex
		latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode" -use-make -output-directory=week\ 9/ week\ 9/Exercises_week_9.tex

week\ 10/Exercises_week_10.pdf: week\ 10/Exercises_week_10.tex
		latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode" -use-make -output-directory=week\ 10/ week\ 10/Exercises_week_10.tex

supplementary\ material/using_git.pdf: supplementary\ material/using_git.tex
		latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode" -use-make -output-directory=supplementary\ material/ supplementary\ material/using_git.tex

clean:
		latexmk -CA
