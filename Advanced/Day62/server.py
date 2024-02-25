from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms import validators
import csv


app = Flask(__name__)
app.secret_key = '6r3hufud3uh2783783'
bootstrap = Bootstrap5(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cafes/')
def get_cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')
        header = next(csv_reader)
        rows = [row for row in csv_reader]
    return render_template('cafes.html', header=header, rows=rows)


@app.route('/add', methods=['GET', 'POST'])
def secret():
    my_form = CreateForm()
    if my_form.validate_on_submit():
        data = [value for key, value in my_form.data.items() if key not in ['submit', 'csrf_token']]
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(data)
    return render_template('add.html', form=my_form)


class CreateForm(FlaskForm):
    name = StringField(label='Cafe Name', validators=[validators.DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)', validators=[validators.URL(message='Invalid URL')])
    open_time = StringField(label='Opening Time e.g 8AM', validators=[validators.DataRequired()])
    close_time = StringField(label='Closing Time e.g 5:30PM', validators=[validators.DataRequired()])
    coffee_rating = SelectField(u'Coffee Rating', choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕️', '☕☕☕☕️☕'],
                                validators=[validators.DataRequired()])
    wifi_rating = SelectField(u'Coffee Rating', choices=['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                              validators=[validators.DataRequired()])
    power_rating = SelectField(u'Coffee Rating', choices=['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌️', '🔌🔌🔌🔌🔌'],
                               validators=[validators.DataRequired()])
    submit = SubmitField(label='Submit')


if __name__ == '__main__':
    app.run(debug=True)
