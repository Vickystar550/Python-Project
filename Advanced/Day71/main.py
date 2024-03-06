from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
import os

app = Flask(__name__)
print(os.environ.get('FLASK_KEY'))
print(os.environ.get('DB_URL'))
app.config['SECRET_KEY'] = os.environ.get('DB_URL')
ckeditor = CKEditor(app)
Bootstrap5(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# Getting images from Gravatar
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    """The Blog Post table"""
    __tablename__: str = "blog_posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # for the relationship between User(parent) and BlogPost(child)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")

    # for the relationship between BlogPost(parent) and Comment(child)
    comments = relationship("Comment", back_populates="parent_post")

    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# Create a User table for all your registered users.
class User(UserMixin, db.Model):
    """The User table"""
    __tablename__: str = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(350), nullable=False)
    name: Mapped[str] = mapped_column(String(250), nullable=False)

    # for the relationship between User(parent) and BlogPost(child)
    posts = relationship("BlogPost", back_populates="author")
    # for the relationship between User(parent) and Comment(child)
    comments = relationship("Comment", back_populates="comment_author")


# Create a new table for user can write a comment
class Comment(db.Model):
    """The Comment table"""
    __tablename__: str = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Relationship between User(parent) and Comment(child)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship(User, back_populates="comments")

    # Relationship between BlogPost(parent) and Comment(child)
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship(BlogPost, back_populates="comments")

    text: Mapped[str] = mapped_column(Text, nullable=False)


# create the schema/tables for the database
with app.app_context():
    db.create_all()


# get current year: for copyright in footer
year = date.today().year
# print(year)


#  Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=['GET', 'POST'])
def register():
    """register a new user for the blog post website"""
    register_form = RegisterForm()
    # for POST request:
    if register_form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        # checking if email already exists:
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hashed_password = generate_password_hash(password=password,
                                                 method='pbkdf2:sha256:600000',
                                                 salt_length=16)
        # store details on the user's table:
        new_user = User(
            email=email,
            password=hashed_password,
            name=name
        )
        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate the user after adding details to the database.
        login_user(new_user)

        # redirect to the home page:
        return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=register_form, year=year)


#  Retrieve a user from the database based on their email.
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Log in user into the blog post website"""
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')

        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            flash("No user with such email, please register", "error")
            return redirect(url_for('register'))
        elif not check_password_hash(pwhash=user.password, password=password):
            flash('Invalid password. please try again', "error")
            return redirect(url_for('login'))
        else:
            login_user(user)
            flash("Successfully logged in")
            return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=login_form, current_user=current_user, year=year)


@app.route('/logout')
def logout():
    """log out user from the blog post website"""
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    """displays all the blog posts on the home page"""
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, current_user=current_user, year=year)


# Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def show_post(post_id):
    """display a particular blog post for comment contribution"""
    comment_form = CommentForm()
    requested_post = db.get_or_404(BlogPost, post_id)

    # if request method is POST
    if comment_form.validate_on_submit():
        # adding to comment table
        new_comment = Comment(
            author_id=current_user.id,
            post_id=post_id,
            text=request.form.get('comment')
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))

    # if request method is GET
    if current_user.is_authenticated:
        return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form, year=year)
    else:
        flash("You need to login or register to comment")
        return redirect(url_for('login'))


# Use a decorator so only an admin user can create a new post
def admin_only(func):
    """checks if current user is an admin"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.id != 1:
            abort(403)
        return func(*args, **kwargs)
    return wrapper


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    """adds new blog post"""
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    # print("adding post")
    return render_template("make-post.html", form=form, year=year)


@app.route('/manage-users')
@admin_only
def manage_users():
    """manage users -- to be accessible by admin only"""
    results = db.session.execute(db.select(User).order_by(User.id))
    users = results.scalars().fetchall()
    return render_template('manage-users.html', users=users, year=year)


@app.route('/delete-user/<int:user_id>', methods=['GET', 'POST'])
@admin_only
def delete_user(user_id):
    """delete user"""
    result = db.get_or_404(User, user_id)

    try:
        db.session.delete(result)
        db.session.commit()
    except IntegrityError:
        flash("Cannot delete user")
    else:
        flash(f"{result.name} successfully deleted")
    finally:
        return redirect(url_for('manage_users'))


# Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    """edit blog post"""
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, year=year)


# Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    """delete a blog post"""
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    """renders the about page"""
    return render_template("about.html", year=year)


@app.route("/contact")
def contact():
    """renders the contact page"""
    return render_template("contact.html", year=year)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
