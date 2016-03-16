# Sliding ball along semicircle with friction

Example on how to embed a bokeh slider by running a bokeh server (requires bokeh 0.11.1).
The app is embeded with a html template "sliding_ball.html".

To see the embeded html page do as follows (in this directory):

1) create the solution data by running:

bash create_solutions.sh

2) compile the html template "sliding_ball.html" (requires doconce):

bash make.sh

3) start a bokeh server:

bokeh serve --allow-websocket-origin=localhost:8000

4) embed the app by running:

python sliding_ball_embed_sliders.py

5) link the page to the url "http://localhost:8000/sliding_ball_embed.html"

python -m SimpleHTTPServer

Now navigate to the local url: "http://localhost:8000/sliding_ball_embed.html"

in your browser.



