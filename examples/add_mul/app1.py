"""
App for giving two numbers to be multiplied and the answer.
The app determines whether the answer is correct of not.
"""

"""
General info:

Python-specific code for an app to be inserted as part of
a bigger flask app.

Define a subclass of Form to define input fields in a form
in the app. This name of the class is only used in this file.

Define some compute function to perform the computations
associated with the input and to return the HTML code
with the results of the computation. The HTML code is
inserted in the view page.

This file *must* define one function:
fill_form_and_result(request, form, result),
where form and result are dictionaries.
The form and the result of the app must define a key
in these dictionaries.
The fill_form_and_result function is called by the
flask app.
"""

from wtforms import Form, FloatField, validators

class InputForm(Form):
    a = FloatField(label='', default=1.0)
    b = FloatField(label='', default=1.0)
    add = FloatField(label='')

# Compute function
def add(a, b, result):
    return 'Correct!' if a + b == result else 'Wrong!'

def fill_form_and_result(request, form, result):
    name = 'add'
    f = form[name] = InputForm(request.form)
    if request.method == 'POST' and f.validate() \
        and request.form['btn'] == 'Check addition':
        result[name] = add(f.a.data, f.b.data, f.add.data)
    else:
        result[name] = None
    # No need to return: in-place changes in form and result dicts
