''' Present an interactive function explorer with slider widgets.

Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.

Use the ``bokeh serve`` command to run the example by executing:

    bokeh serve sliders.py

at your command prompt. Then navigate to the URL

    http://localhost:5006/sliders

in your browser.

'''

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
N = 200
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
tau = Slider(title="tau", value=0.0, start=0, end=10.0, step=0.1)
print mu.value

# Set up callbacks

def update_data(attrname, old, new):

    # Get the current slider values
    mu_v = mu.value
    tau_v = tau.value
    dtau = 0.1
    N = round(tau_v/dtau)
    mu_str = str(mu_v)
    if mu_str =='1':
        mu_str = '1.0'
    if mu_str =='0':
        mu_str = '0.0'
        
    textFile_name = '../data/' + mu_str + '.txt'
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

    degree_rad = acos(-x[0])
    degree_normal = round(degree_rad*180./pi)
    plot.title = titlevalue + str(degree_normal)

    source.data = dict(x=x, y=y)

for w in [mu, tau]:
    w.on_change('value', update_data)


# Set up layouts and add to document
inputs = VBoxForm(children=[mu, tau])

layout = HBox(children=[inputs, plot], width=800)

html = """
<html>
    <head>Yolo</head>
    <body>
        %s
    </body>
</html>
""" % autoload_server(layout, session_id=session.id)

with open("motion.html", "w+") as f:
    f.write(html)
    
document.add_root(layout)
if __name__ == "__main__":
    print("\npress ctrl-C to exit")
    session.loop_until_closed()
