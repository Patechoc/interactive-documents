### Running a DocOnce document with interactive plots

In an interactive Unix shell, set some variables to save typing:


```
Terminal> name=ibplots
Terminal> opts=''
Terminal> html_opts='--html_style=bootstrap --html_code_style=inherit'
```

Clean all redundant DocOnce files:


```
Terminal> doconce clean
```

Start Bokeh server in the background (and wait a bit):


```
Terminal> bokeh serve --allow-websocket-origin=localhost:8000 &
```

Translate the DocOnce document to HTML format (make sure `doconce format`
command is run in the background and that `doconce split_html` is not):


```
Terminal> doconce format html $name $html_opts &
Terminal> doconce split_html $name --nav_button=text --method=split
```

Finally, start


```
Terminal> python -m SimpleHTTPServer &
```

Error messages from this command saying that `Address is already in use`
are normal.

You are now ready to read the document by loading `ibplots.html` into
a web browser at the address





Look at the log file `ibplots.dlog` to examine what interactive plots were
recognized and processed.

