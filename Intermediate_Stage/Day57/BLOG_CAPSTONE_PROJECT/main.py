from flask import Flask, render_template
from post import Post


app = Flask(__name__)

post = Post()


@app.route('/')
def home():
    return render_template("index.html", blog_posts=post.blogs)


@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    return render_template('post.html', post_data=post.retrieve_blog(id_=blog_id))


if __name__ == "__main__":
    app.run(debug=True)
