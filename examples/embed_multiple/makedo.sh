#!/bin/sh
set -x
name=template
name=tmp
bokeh serve --allow-websocket-origin=localhost:8000 &
doconce format html $name &
python -m SimpleHTTPServer &

echo "Navigate to: http://localhost:8000/$name.html"
