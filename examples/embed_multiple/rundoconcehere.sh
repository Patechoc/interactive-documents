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


name=template

doconce format html $name --pygments_html_style=default SLIDE_TYPE=reveal SLIDE_THEME=simple
doconce slides_html $name reveal --html_slide_theme=simple
#compile $name 
#--keep_pygments_html_bg
