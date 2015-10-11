Very simple proof-of-concept of how to make an interactive document with
multiple apps in flask.

Run like this:

```
Terminal> python controller.py
```
Open the URL in a browser.

There are two apps, `app1` and `app2`, each represented as a module and
an HTML ``view'' file for how to render the results of the app.
The main document is `templates/view.html` which contains text and
appropriate Jinja2 code for the apps.

One could think that `templates/template.html` is some DocOnce-like
document with commands like `INCLUDE: app1` for including apps. Here
we have an external script `generate_view.py` that can insert the
`app1.html` and `app2.html` files into `templates/template.html` to
create the final document `templates/view.html`

It is straightforward to extend DocOnce with functionality such that
includes apps using the setup in this directory.
