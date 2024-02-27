from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # fetch all records in the database
    with app.app_context():
        result = db.session.execute(db.select(Book))
        records = result.scalars().fetchall()
        # initializing a list to store the records
        all_books = []
        for record in records:
            all_books.append({
                'id': record.id,
                'title': record.title,
                'author': record.author,
                'rating': record.rating
            })
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        #  create new record to the database
        with app.app_context():
            new_book = Book(title=request.form.get('title'),
                            author=request.form.get('author'),
                            rating=request.form.get('rating')
                            )
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'), code=302)
    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit_rating():
    if request.method == 'POST':
        # update the new rating to the database for a given book id
        book_id = request.form.get('id')
        new_rating = request.form.get('rating')

        with app.app_context():
            book_to_update = db.get_or_404(Book, book_id)
            book_to_update.rating = new_rating
            db.session.commit()
        return redirect(url_for('home'), code=302)
    else:
        # retrieving book with id_
        id_ = request.args.get('id')

        with app.app_context():
            book = db.session.execute(db.select(Book).where(Book.id == id_)).scalar()
            book_item = {
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'rating': book.rating
            }
        return render_template('edit.html', item=book_item)


@app.route('/delete/<int:id_>')
def delete_item(id_):
    book_id = id_
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'), code=302)


if __name__ == "__main__":
    app.run(debug=True)
