#!/bin/bash

Template=template
#code=embed.py

doconce format html $Template

bokeh serve --allow-websocket-origin=localhost:8000 &

python Main.py &

python -m SimpleHTTPServer &

echo "Navigate to: http://localhost:8000/embed_$Template.html"
