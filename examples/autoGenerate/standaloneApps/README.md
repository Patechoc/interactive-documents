First example on how one could auto-generate an interactive bokeh plot from a doconce tag IBPLOT:[plot info]

This is not yet coupled with doconce, but is a first example/test on how auto-generating bokeh-plots from info in a line in a .do.txt file.

1) Create the app by running:

bokeh serve --show generatFromFile.py

2) A browser should now open showing the app:

3) Out-comment one of the other IBPLOT tags in IBPLOT.do.txt, and comment out all other to generate a different plot. Run command 1) again to generate a new app.

3) Write a new line for a different curve in IBPLOT.do.txt and test

the syntax is:

IBPLOT:[y=f(x, var1, var2, ..);x='x';xrange=(start, stop);,yrange=(start, stop),sliders=dict(var1="title='var1', value=first_value_of_Var1, start=min_value, end=max_value", var2="title='var2', value=1, start=0.1, end=2")]




