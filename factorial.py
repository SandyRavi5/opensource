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
    name = False
    factorial=0
    form = InfoForm()
    if form.validate_on_submit():
        number = form.number.data
        form.number.data = ''
        def factorial(number):
            if(number==1):
                return 1
            else:
                return(number*factorial(number-1))
        fact= factorial(number)
    return render_template('display1.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
