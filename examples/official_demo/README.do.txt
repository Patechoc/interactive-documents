======= Running a DocOnce document with interactive plots =======

In an interactive Unix shell, set some variables to save typing:

!bc sys
Terminal> name=ibplots
Terminal> opts=''
Terminal> html_opts='--html_style=bootstrap --html_code_style=inherit'
!ec

Clean all redundant DocOnce files:

!bc sys
Terminal> doconce clean
!ec

Start Bokeh server in the background (and wait a bit):

!bc sys
Terminal> bokeh serve --allow-websocket-origin=localhost:8000 &
!ec

Translate the DocOnce document to HTML format (make sure `doconce format`
command is run in the background and that `doconce split_html` is not):

!bc sys
Terminal> doconce format html $name $html_opts &
Terminal> doconce split_html $name --nav_button=text --method=split
!ec
Finally, start

!bc sys
Terminal> python -m SimpleHTTPServer &
!ec
Error messages from this command saying that `Address is already in use`
are normal.

You are now ready to read the document by loading `ibplots.html` into
a web browser at the address

!bbox
!bc
http://localhost:8000/ibplots.html
!ec
!ebox
