'''
Created on Jun 9, 2016

@author: fredrik
'''

from bokeh.document import Document
from bokeh.client import push_session
from bokeh.embed import autoload_server
from bokeh.models import HBox, VBoxForm

from parser import find_tags
from SetupApp import CreateApp

document = Document()
session = push_session(document)

file_name = "template"

IBPLOT_tags = find_tags(file_name + ".html")

appLayoutList = []

for app_info in IBPLOT_tags:

    app = CreateApp(app_info)

    for w in app.sliderList:
        w.on_change('value', app.update_data)

    inputs = VBoxForm(children=app.sliderList)

    layout = HBox(children=[inputs, app.plot], width=800)
    document.add_root(layout)
    appLayoutList.append(layout)

# embed app in html template
old_file = file_name + ".html"
new_file = "embed_" + file_name +".html"
f1 = open(old_file, "r")
f2 = open(new_file, "w+")

appNumber = 0
for line in f1:
    if 'IBPLOT' in line and line[0] != '#' and line[0] != '<':
        f2.write("<p>This app is created by the following tag: </p>")
        f2.write("<p>")
        f2.write(line)
        f2.write("</p>")
        f2.write(autoload_server(appLayoutList[appNumber], session_id=session.id))
        appNumber += 1

    else:
        f2.write(line)
f1.close()
f2.close()



document.add_root(layout)

if __name__ == "__main__":
    print "runnign on: http://localhost:8000/" + new_file
    session.loop_until_closed()
