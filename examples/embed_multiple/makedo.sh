#!/bin/sh
name=template
bokeh serve --allow-websocket-origin=localhost:8000 &
doconce format html $name --IBPLOT
python -m SimpleHTTPServer &

echo "Navigate to: http://localhost:8000/$name.html"
