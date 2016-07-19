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
import inspect
from bokeh.plotting import Figure
from bokeh.models import ColumnDataSource, HBox, VBoxForm
from bokeh.models.widgets import Slider, TextInput
from bokeh.io import curdoc

class CreateApp():

    def __init__(self, plot_info):


        N = 200
        colors = ['red', 'green', 'indigo', 'orange', 'blue', 'grey', 'purple']
        possible_inputs = ['x_axis_label', 'xrange', 'yrange', 'sliderDict', 'title', 'number_of_graphs']

        y = None
        if ".py" in plot_info[0]:
            print "handling .pyfile"
            compute = None
            exec("from " + plot_info[0][0:-3] + " import compute")
            arg_names = inspect.getargspec(compute).args
            argString = ""
            for n, arg in enumerate(arg_names):
                argString = argString + arg
                if n != len(arg_names) - 1:
                    argString = argString + ", "
            computeString = "y = compute(" + argString + ")"
            self.computeString = computeString
            self.compute = compute

        self.curve = plot_info[0]
        x_axis_label = None
        y_axis_label = None
        xrange = (0, 10)
        yrange = (0, 10)
        sliderDict = None
        title = None
        number_of_graphs = None
        legend = None
        reverseAxes = False

        self.source = []
        self.sliderList = []


        for n in range(1,len(plot_info)):
            # Update inputs
            exec(plot_info[n].strip())

        if reverseAxes:
            self.x = np.linspace(yrange[0], yrange[1], N)
        else:
            self.x = np.linspace(xrange[0], xrange[1], N)

        self.reverseAxes = reverseAxes
        if sliderDict != None:
            self.parameters = sliderDict.keys()

            for n, param in enumerate(self.parameters):
                exec("sliderInstance = Slider(" + sliderDict[param] + ")") # Todo: Fix so exec is not needed
                exec("self.sliderList.append(sliderInstance)") # Todo: Fix so exec is not needed

                # get first value of param
                exec(param + " = "  + 'self.sliderList[n].value') # Todo: Fix so exec is not needed

        # Set up plot
        self.plot = Figure(plot_height=400, plot_width=400, title=title,
                      tools="crosshair,pan,reset,resize,save,wheel_zoom",
                      x_range=xrange, y_range=yrange)
        self.plot.xaxis.axis_label = x_axis_label
        self.plot.yaxis.axis_label = y_axis_label
        # generate the first curve:
        x = self.x
        if ".py" in plot_info[0]:
            exec(computeString)
        else:
            exec(plot_info[0]) #  execute y = f(x, params)

        if type(y) is list:
            if legend == None:
                legend = [legend]*len(y)
            for n in range(len(y)):

                if self.reverseAxes:
                    x_plot = y[n]
                    y_plot = self.x
                else:
                    x_plot = self.x
                    y_plot = y[n]
                self.source.append(ColumnDataSource(data=dict(x=x_plot, y=y_plot)))
                self.plot.line('x', 'y', source=self.source[n], line_width=3, line_color=colors[n], legend=legend[n])
        else:
            if self.reverseAxes:
                x_plot = y
                y_plot = self.x
            else:
                x_plot = self.x
                y_plot = y
            self.source.append(ColumnDataSource(data=dict(x=x_plot, y=y_plot)))
            self.plot.line('x', 'y', source=self.source[0], line_width=3, legend=legend)



    def update_data(self, attrname, old, new):

        # Get the current slider values

        y = None
        x = self.x
        for n, param in enumerate(self.parameters):
            exec(param + " = "  + 'self.sliderList[n].value')
        # generate the new curve:

        if ".py" in self.curve:
            compute = self.compute
            exec(self.computeString) #  execute y = compute(x, params)
        else:
            exec(self.curve) #  execute y = f(x, params)

        if type(y) is list:
            for n in range(len(y)):
                if self.reverseAxes:
                    x_plot = y[n]
                    y_plot = self.x
                else:
                    x_plot = self.x
                    y_plot = y[n]
                self.source[n].data = dict(x=x_plot, y=y_plot)
        else:
            if self.reverseAxes:
                x_plot = y
                y_plot = x
            else:
                x_plot = x
                y_plot = y
            self.source[0].data = dict(x=x_plot, y=y_plot)
