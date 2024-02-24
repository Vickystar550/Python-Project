from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

response = requests.get(url='https://api.npoint.io/674f5423f73deab1e9a7')
blogs = response.json()

date_ = datetime.datetime.today()

calender_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
                   'September', 'October', 'November', 'December']

month = calender_months[date_.month - 1]

date_str = f"{month} {date_.day}, {date_.year}"


@app.route('/')
def home():
    return render_template('index.html', posts=blogs, year_quote=date_str)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def get_post(post_id):
    for blog in blogs:
        if blog['id'] == post_id:
            return render_template('post.html', post=blog, year_quote=date_str)


if __name__ == "__main__":
    app.run(debug=True)
