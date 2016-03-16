# interactive-documents

Ideas and tests for how to make interactive (DocOnce) documents, e.g.,
with flask.

## Contents

 * Proof-of-concept how to let a document be a flask app with multiple apps,
   se `examples/add_mul`.
 * A not-yet-working example on how to embed *interactive*
   bokeh plots on bokeh-servers in a flask app (`examples/bokeh_sliders`).
 * A working example on how to embed *interactive* bokeh apps using a bokeh-server, and the bokeh (0.11.1) autoload_server ( examples/sliding_ball )
## Goal

The goal of this project is to establish recipes such that DocOnce
documents can feature interactive applications. The `examples/add_mul`
example shows the principle, but of particular interest is to
embed multiple *interactive* bokeh plots in a DocOnce document.
This will (based on the ideas in `examples/add_mul`) require
embedding an app like `examples/bokeh_sliders/sliders_app.py` in
a flask app, but how to do this is yet an open question.

An alternative approach is to drop integrating interactive bokeh server
apps into a flask app, but instead embed these server apps directly
in HTML using iframes:

```
    <div>
    <iframe
        src="http://demo.bokehplots.com:5006/bokeh/sliders/#"
        frameborder="0"
        style="overflow:hidden;height:460px;width: 120%;
        -moz-transform: scale(0.85, 0.85);
        -webkit-transform: scale(0.85, 0.85);
        -o-transform: scale(0.85, 0.85);
        -ms-transform: scale(0.85, 0.85);
        transform: scale(0.85, 0.85);
        -moz-transform-origin: top left;
        -webkit-transform-origin: top left;
        -o-transform-origin: top left;
        -ms-transform-origin: top left;
        transform-origin: top left;"
        height="460"
    ></iframe>
    </div>
```

How to organize all the potential interactive bokeh apps on some other
server is an open question.

It seems most promising to integrate `sliders_app.py` type of code
as an app in the setup in `examples/add_mul`.

## References

 * [Using Web Frameworks for Scientific Applications](http://hplgit.github.io/web4sciapps/doc/pub/sphinx-basicstrap/index.html)
 * [Embedding a bokeh app in flask](http://stackoverflow.com/questions/29949712/embedding-a-bokeh-app-in-flask) (does not provide answer to *interactive* apps, just basic plots with the standard interactivity, but that can easier be embedded directly with HTML code)
 * [Embedding bokeh plots in a flask app](https://github.com/bokeh/bokeh/blob/master/examples/embed/slideshow/app_reveal.py) (plots with interactivity are inserted in a flask app, but a bit different from the `sliders_app.py` example)
 * [Bokeh plots in DocOnce](http://hplgit.github.io/doconce/doc/pub/manual/manual.html#___sec9) (browse downwards to the section "Interactive Bokeh Plots for HTML")
