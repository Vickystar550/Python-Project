from flask import Flask, render_template, redirect, url_for, request
import requests
import random
from datetime import date

app = Flask(__name__)

year = date.today().year
print(year)


@app.route('/')
def home():
    return render_template('index.html', page_name='homepage', copyright_year=year)


@app.route('/about')
def about():
    return render_template('about.html', page_name='aboutpage', copyright_year=year)


@app.route('/contact')
def contact():
    return render_template('contact.html', page_name='contactpage', copyright_year=year)


@app.route('/experience')
def experience():
    return render_template('work_experience.html', page_name='work_experience', copyright_year=year)


@app.route('/my_skills')
def my_skills():
    return render_template('skills.html', page_name='skills_page', copyright_year=year)


@app.route('/education')
def education():
    return render_template('education.html', page_name='education_page', copyright_year=year)


@app.route('/interest', methods=['POST', 'GET'])
def interest():
    if request.method == 'POST':
        # get form input
        email = request.form.get('email')
        print(email)

        # adding email to database:

        return redirect(url_for('home'), code=302)
    return render_template('interest.html', page_name='interest_page', copyright_year=year)


if __name__ == "__main__":
    app.run(debug=True)
