from sliders_app import SlidersApp
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    pass
    app2 = SlidersApp.create()
    print dir(app2)
    return app2
    #return render_template('view.html',
    #                       form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
