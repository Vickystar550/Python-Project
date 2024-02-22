from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

date_ = datetime.now().year


@app.route('/')
def home():
    number = random.randint(1, 100)
    return render_template('home.html', num=number, year=date_)


@app.route('/guess/<name>')
def prediction(name):
    age = requests.get(url=f'https://api.agify.io?name={name}').json().get('age')
    gender = requests.get(url=f'https://api.genderize.io?name={name}').json().get('gender')
    return render_template('prediction.html', year=date_, name=name, age=age, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = ' https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url=blog_url)
    blog_posts = response.json()
    return render_template('blog.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(debug=True)
