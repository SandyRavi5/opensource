from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
class InfoForm(FlaskForm):
    number=IntegerField("Enter the number")
    submit = SubmitField('Submit')
@app.route('/', methods=['GET', 'POST'])
def index():
    number = False
    form = InfoForm()
    if form.validate_on_submit():
        number = form.number.data
        form.number.data = ''
        def Fibonacci(n):
            if n==0:
                return 0
            elif n==1:
                return 1
            else:
                return (Fibonacci(n-1)+Fibonacci(n-2))
        fib=Fibonacci(number)
    return render_template('display2.html', **locals())
if __name__ == '__main__':
    app.run(debug=True)
