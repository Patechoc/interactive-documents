#!/bin/sh
set -x
name=template
doconce clean
bokeh serve --allow-websocket-origin=localhost:8000 &
sleep 8  # wait for bokeh serve
doconce format html $name &
doconce split_html $name --nav_button=text --method=split
python -m SimpleHTTPServer &

echo "Navigate to: http://localhost:8000/$name.html"
