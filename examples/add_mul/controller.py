from flask import Flask, render_template, request

# Import all apps
import app1
import app2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = {}
    result = {}

    # Process all apps
    app1.fill_form_and_result(request, form, result)
    app2.fill_form_and_result(request, form, result)

    return render_template('view.html',
                           form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
