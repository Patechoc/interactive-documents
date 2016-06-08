# Sliding ball along semicircle with friction

Example on how to embed a bokeh slider by running a bokeh server (requires bokeh 0.11.1).
The app is embeded with a html template "sliding_ball.html".

To see the embeded html page do as follows (in this directory):

1) compile the html template "sliding_ball.html" (requires doconce):

doconce format html template.do.txt

2) start a bokeh server:

bokeh serve --allow-websocket-origin=localhost:8000

3) embed the app by running:

python sliding_ball_embed_sliders.py

4) link the page to the url "http://localhost:8000/embed_template.html"

python -m SimpleHTTPServer

Now navigate to the local url: "http://localhost:8000/embed_template.html"

in your browser.



