from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
class InfoForm(FlaskForm):

    name = StringField('Enter the name.')
    password=PasswordField('enter password')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = False
    password=False
    form = InfoForm()
    if form.validate_on_submit():
        name = form.name.data
        password=form.password.data
        form.name.data = ''
    return render_template('display.html',password=password,name=name,form=form)


if __name__ == '__main__':
    app.run(debug=True)
