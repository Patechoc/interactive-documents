#!/bin/bash
# Translate .tex files in .. to doconce
set -x  # Show all commands prior to execution
#
function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}


#code=vrb
code=pyg

pdf_opt="-shell-escape"
options="--no_abort  --encoding=utf-8 --allow_refs_to_external_docs"


function compile {
name=$1
system doconce format pdflatex $name --latex_code_style=$code $options 

system doconce replace '10pt]{article}' '12pt, a4paper]{book}' $name.tex
system doconce replace 'linenos=false' 'linenos=True' $name.tex
system doconce replace '${bbox()}' '' $name.tex
system doconce replace '${ebox()}' '' $name.tex

linenos=false




system pdflatex $pdf_opt $name
system makeindex $name
#system bibtex $name
system pdflatex $pdf_opt $name
system pdflatex $pdf_opt $name

}
function generate_html {
name=$1
doconce format html $name --html_style=bootstrap_bluegray  --html_links_in_new_window --device=screen  --html_figure_hrule=none --html_DOCTYPE --encoding=utf-8 --without_solutions --html_bootstrap_navbar=off
}

name=sliding_ball

generate_html $name

#compile $name 

