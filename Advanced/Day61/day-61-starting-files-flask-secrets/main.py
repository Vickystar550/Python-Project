from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.secret_key = '7843h4uuf899urpfj2o309'
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[validators.Email(message="Invalid email address")])
    password = PasswordField(label='Password', validators=[validators.Length(min=8, message="Field must be at least 8 "
                                                                                            "characters long")])
    submit = SubmitField(label='Log in')


if __name__ == '__main__':
    app.run(debug=True)
