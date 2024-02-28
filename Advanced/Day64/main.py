from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
import requests
from sqlalchemy.exc import IntegrityError


TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMDhlMzA2MGQ3ZWY4ZWFkOGZjM2ViNGRjZWRlMjk4ZiIsInN1YiI6IjY1ZGU2NzcyM2ZmMmRmMDE4NzBiZDVhNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Z5pjHhtbitAfjv5vKlge-OGgxJtj6gzktnB3WPp-W8Y'


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


# with app.app_context():
#     new_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family ("
#                     "Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each "
#                     "other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print("Waiting")
    # fetch all records in the database
    with app.app_context():
        result = db.session.execute(db.select(Movie))
        records = result.scalars().fetchall()
        # initializing a list to store the records
        all_movies = []
        for record in records:
            all_movies.append({
                'id': record.id,
                'title': record.title,
                'year': record.year,
                'description': record.description,
                'rating': record.rating,
                'ranking': record.ranking,
                'review': record.review,
                'img_url': record.img_url
            })
    return render_template("index.html", movies=all_movies)


class EditMovieForm(FlaskForm):
    new_rating = StringField('Your Rating Out of 10 e.g 7.5', validators=[DataRequired()])
    new_review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


@app.route('/add', methods=['GET', 'POST'])
def add():
    movie_form = AddMovieForm()
    if request.method == 'POST':
        if movie_form.validate_on_submit():
            title = movie_form.data.get('movie_title')
            tmdb_movies = search_movies(query=title)
            print(tmdb_movies)
            return render_template('select.html', movies_list=tmdb_movies)
    return render_template('add.html', form=movie_form)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditMovieForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            movie_id = int(request.form.get('id'))
            with app.app_context():
                movie_to_update = db.get_or_404(Movie, movie_id)
                movie_to_update.rating = request.form.get('new_rating')
                movie_to_update.review = request.form.get('new_review')
                db.session.commit()
        return redirect(url_for('home'), code=302)

    id_ = request.args.get('id')
    with app.app_context():
        movie = db.session.execute(db.select(Movie).where(Movie.id == id_)).scalar()
    return render_template('edit.html', form=form, movie=movie)


@app.route('/delete')
def delete():
    movie_id = int(request.args.get('id'))
    with app.app_context():
        movie_to_delete = db.get_or_404(Movie, movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'), code=302)


def search_movies(query):
    url = "https://api.themoviedb.org/3/search/movie"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    parameters = {
        'query': f'{query}',
    }
    response = requests.get(url, headers=headers, params=parameters)
    movies_raw_data = response.json().get('results')

    return [{
        "id_": data.get('id'),
        "title": data.get("title"),
        "description": data.get("overview"),
        "release_year": data.get("release_date")
    } for data in movies_raw_data]


@app.route('/getmovie', methods=['GET', 'POST'])
def get_movie_details():
    movie_id = request.args.get('id')
    if movie_id:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TOKEN}"
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        # adding to database:
        with app.app_context():
            new_movie = Movie(
                title=data.get("title"),
                year=int(data.get("release_date").split("-")[0]),
                description=data.get("overview"),
                img_url=f"https://image.tmdb.org/t/p/w500{data.get('poster_path')}"
            )

            db.session.add(new_movie)
            db.session.commit()
            # except IntegrityError:
            #     print("could not add to database")
            #     db.session.rollback()

        return redirect(url_for('edit'), code=302)


if __name__ == '__main__':
    app.run(debug=True)
