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

from bokeh.plotting import Figure
from bokeh.models import ColumnDataSource, HBox, VBoxForm
from bokeh.models.widgets import Slider, TextInput
from bokeh.io import curdoc


# open .do.txt file to get data:

with open('IBPLOT.do.txt', 'r') as f:
    
    for line in f:
        if 'IBPLOT' in line and line[0] != '#':
            plot_info = line[8:-1].split(';')
            
new_plot_info = []
for element in plot_info:
    if element[0]==' ':
        element = element[1:]
    if element[-1]==' ':
        element = element[:-1]
    if element[-1] == ']':
        element = element[:-1]
    new_plot_info.append(element)
    print element
    
    
exec(new_plot_info[2]) # xrange
exec(new_plot_info[3]) # yrange
exec(new_plot_info[4]) # dictionary containg info about slider values for each parameter

# Set up data
N = 200
x = np.linspace(xrange[0], xrange[1], N)


# Set up plot
plot = Figure(plot_height=400, plot_width=400, title=new_plot_info[0],
              tools="crosshair,pan,reset,resize,save,wheel_zoom",
              x_range=xrange, y_range=yrange)


# Set up widgets
params = sliders.keys()
Slider_instances = []

for n, param in enumerate(params):
    
    # create a global Slider instance for each parameter:
    exec('param{0}'.format(n) + " = Slider(" + sliders[param] + ")")
    
    
    Slider_instances.append(eval('param{0}'.format(n))) # add Slider to list
    # get the first value for all parameters:
    exec(param + " = "  + 'param{0}.value'.format(n))

# generate the first curve:
exec(new_plot_info[0]) #  execute y = f(x, params)
source = ColumnDataSource(data=dict(x=x, y=y))
plot.line('x', 'y', source=source, line_width=5, color='navy', line_alpha=0.6)


# Set up callbacks


def update_data(attrname, old, new):

    # Get the current slider values
    
    for n, param in enumerate(params):
        # get all parameter values:
        exec(param + " = "  + 'param{0}.value'.format(n))

    # Generate the new curve:
    exec(new_plot_info[0])  #  execute y = f(x, params)


    source.data = dict(x=x, y=y)

for w in Slider_instances:
    w.on_change('value', update_data)


# Set up layouts and add to document
inputs = VBoxForm(children=Slider_instances)

curdoc().add_root(HBox(children=[inputs, plot], width=800))
