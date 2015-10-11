"""
App for giving two numbers to be multiplied and the answer.
The app determines whether the answer is correct of not.
"""

from wtforms import Form, FloatField, validators

class InputForm(Form):
    p = FloatField(label='', default=2)
    q = FloatField(label='', default=2)
    mul = FloatField(label='')

# Compute function
def mul(p, q, result):
    return 'Correct!' if p*q == result else 'Wrong!'

def fill_form_and_result(request, form, result):
    name = 'mul'
    f = form[name] = InputForm(request.form)
    if request.method == 'POST' and f.validate() \
        and request.form['btn'] == 'Check multiplication':
        result[name] = mul(f.p.data, f.q.data, f.mul.data)
    else:
        result[name] = None
