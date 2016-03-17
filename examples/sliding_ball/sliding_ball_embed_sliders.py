''' This is an example on how to embed a slider app in a html template.

Scrub the sliders to see where the ball end up.

in order to see the html with the embeded app do as follows.

1) create the solution data by running:

bash create_solutions.sh

2) compile the html template "sliding_ball.html":

bash make.sh

3) start a bokeh server:

bokeh serve --allow-websocket-origin=localhost:8000

4) embed the app by running:

python sliding_ball_embed_sliders.py

5) link the page to the url "http://localhost:8000/sliding_ball_embed.html"

python -m SimpleHTTPServer

Now navigate to the local url: "http://localhost:8000/sliding_ball_embed.html"

in your browser.

'''
from __future__ import print_function

import numpy as np

from bokeh.document import Document
from bokeh.client import push_session
from bokeh.plotting import Figure
from bokeh.models import ColumnDataSource, HBox, VBoxForm
from bokeh.models.widgets import Slider
from math import sin, cos, pi, acos
from bokeh.embed import autoload_server

document = Document()
session = push_session(document)
# Set up data
x = [-1.]
y = [0.]
source = ColumnDataSource(data=dict(x=x, y=y))


# Set up plot
plot = Figure(plot_height=500, plot_width=500, title="ball sliding along semicircle, angle=0",
              tools="crosshair,pan,reset,resize,save,wheel_zoom",
              x_range=[-1.1, 1.1], y_range=[-1.1, 1.1])

plot.circle('x', 'y', source=source, size=10, color='navy', line_alpha=0.6)

theta_line = np.linspace(0, pi, 101)
plot.line(-np.cos(theta_line), -np.sin(theta_line), line_width=2)



# Set up widgets
titlevalue = 'ball sliding along semicircle, angle='
mu = Slider(title="mu", value=0.0, start=0, end=1, step=0.1)
tau = Slider(title="tau", value=0.0, start=0, end=20.0, step=0.1)

dtau = tau.step
# Set up callbacks

def update_data(attrname, old, new):

    # Get the current slider values
    mu_v = mu.value
    tau_v = tau.value
    N = round(tau_v/dtau)
    mu_str = str(mu_v)
    if mu_str =='1':
        mu_str = '1.0'
    if mu_str =='0':
        mu_str = '0.0'
        
    textFile_name = 'data/' + mu_str + '.txt'
    with open(textFile_name, 'r') as filename:
        n = 0
        for line in filename:
            if n == N:
                theta = float(line.split()[1])
            n += 1
            
    filename.close()
    # Generate the new curve
    x = [-cos(theta)]
    y = [-sin(theta)]

    angle_rad = acos(-x[0])
    angle_degree = round(angle_rad*180./pi)
    plot.title = titlevalue + str(angle_degree)

    source.data = dict(x=x, y=y)

for w in [mu, tau]:
    w.on_change('value', update_data)


# Set up layouts and add to document
inputs = VBoxForm(children=[mu, tau])

layout = HBox(children=[inputs, plot], width=800)

# embed app in html template
old_file = "sliding_ball.html"
new_file = "sliding_ball_embed.html"
f1 = open(old_file, "r")
f2 = open(new_file, "w+")

for line in f1:
    if "APP: [sliding_ball]" in line:
        f2.write(autoload_server(layout, session_id=session.id))
    else:
        f2.write(line)
f1.close()
f2.close()
    
print(__doc__)

document.add_root(layout)

if __name__ == "__main__":
    print("\npress ctrl-C to exit")
    session.loop_until_closed()
