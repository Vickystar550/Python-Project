from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


class PostForm(FlaskForm):
    """create a form object to add new blogpost"""
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired(), URL("Enter a valid URL")])
    blog_content = CKEditorField('Blog Content')
    submit = SubmitField("SUBMIT POST")


# create the schema
with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def get_all_posts():
    """get all the blogpost records in the database"""
    posts = db.session.execute(db.select(BlogPost)).scalars().fetchall()
    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:post_id>', methods=['GET'])
def show_post(post_id):
    """show a blogpost with given the post_id"""
    requested_post = db.session.get(BlogPost, post_id)
    if requested_post:
        return render_template("post.html", post=requested_post)


@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    """adds new blogpost to the database"""
    # create the PostForm object
    post_form = PostForm()

    # if the request method is POST,
    if request.method == 'POST':
        if post_form.validate_on_submit():
            # initialize a new BlogPost Table Object i.e record
            new_blog = BlogPost(
                title=request.form.get('title'),
                subtitle=request.form.get('subtitle'),
                date=datetime.now().strftime('%B %d, %Y'),
                body=request.form.get('blog_content'),
                author=request.form.get('author'),
                img_url=request.form.get('img_url')
            )
            db.session.add(new_blog)
            db.session.commit()
            return redirect(url_for('get_all_posts'), code=302)
    return render_template('make-post.html', form=post_form, is_edit=False)


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    """edit a blogpost with an id = post_id"""
    post = db.session.get(BlogPost, post_id)
    post_id = post.id

    # make an edit_form object out of PostForm class
    edit_form = PostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body_content=post.body
    )

    # if request method is POST and edit_form's validation on submission is successful
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.body = edit_form.blog_content.data
        print(post.body)
        print(request.form.get('ckeditor'))
        post.author = edit_form.author.data
        post.img_url = edit_form.img_url.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id), code=302)

    # render this if request method is GET
    return render_template('make-post.html', form=edit_form, is_edit=True, id_=post_id)


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    """delete a blogpost with an id = post_id"""
    post = db.session.get(BlogPost, post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'), code=302)


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
