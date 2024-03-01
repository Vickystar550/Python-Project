from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import random


TOKEN = 'add your api token here'

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
    """Create the database table"""
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


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

        # Editing ranking base on the rating.
        # Highest move rate gets the highest rank
        sorted_rates = sorted([movie.get('rating') for movie in all_movies], reverse=True)
        enumerated_rates_list = [item for item in enumerate(sorted_rates, start=1)]

        for movie in all_movies:
            for item in enumerated_rates_list:
                if movie.get('rating') == item[1]:
                    movie['ranking'] = item[0]
        # print(all_movies)

        # another way of doing this is:
        # result = db.session.execute(db.select(Movie).order_by(Movie.rating))
        # all_movies = result.scalars().all()  # convert ScalarResult to Python List
        #
        # for i in range(len(all_movies)):
        #     all_movies[i].ranking = len(all_movies) - i
        # db.session.commit()
    return render_template("index.html", movies=all_movies)


class EditMovieForm(FlaskForm):
    """create a flask_wtf form to edit movie details"""
    new_rating = StringField('Your Rating Out of 10 e.g 7.5', validators=[DataRequired()])
    new_review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    """a flask_wtf form to add a new movie"""
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


@app.route('/add', methods=['GET', 'POST'])
def add():
    """adds a new movie"""
    # create a movie flask_wtf form object
    movie_form = AddMovieForm()
    # if the request method to this route is POST,
    if request.method == 'POST':
        if movie_form.validate_on_submit():     # and the form is validated and submitted:
            title = movie_form.data.get('movie_title')
            tmdb_movies = search_movies(query=title)
            # print(tmdb_movies)
            return render_template('select.html', movies_list=tmdb_movies)
    return render_template('add.html', form=movie_form)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    """edit a movie details"""
    form = EditMovieForm()
    # if request method is POST and form submission is validated,
    if request.method == 'POST':
        if form.validate_on_submit():
            # get movie id from the request form id
            movie_id = int(request.form.get('id'))
            with app.app_context():
                # add edited details to the edited movie record
                movie_to_update = db.get_or_404(Movie, movie_id)
                movie_to_update.ranking = int(request.form.get('new_ranking'))
                movie_to_update.rating = float(request.form.get('new_rating'))
                movie_to_update.review = request.form.get('new_review')
                db.session.commit()
        # redirect to the home page
        return redirect(url_for('home'), code=302)

    # if request method is GET, get the request args for id
    id_ = request.args.get('id')
    with app.app_context():
        # get the movie record object and send it over to the rendered templates
        movie = db.session.execute(db.select(Movie).where(Movie.id == id_)).scalar()
    return render_template('edit.html', form=form, movie=movie)


@app.route('/delete')
def delete():
    """delete a movie from the database"""
    movie_id = int(request.args.get('id'))
    with app.app_context():
        movie_to_delete = db.get_or_404(Movie, movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
    # redirecting to the home page
    return redirect(url_for('home'), code=302)


def search_movies(query):
    """Search the TMDB for a movie and associated info"""
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
    """Get more details of a movie via TMDB"""
    movie_id = request.args.get('id')
    if movie_id:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TOKEN}"
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        # adding to a database the search movie required details:
        with app.app_context():
            new_movie = Movie(
                title=data.get("title"),
                year=int(data.get("release_date").split("-")[0]),
                description=data.get("overview"),
                rating=round(random.uniform(5, 10), 1),
                ranking=random.randint(1, 10),
                review='to be added',
                img_url=f"https://image.tmdb.org/t/p/w500{data.get('poster_path')}"
            )
            db.session.add(new_movie)
            db.session.commit()
        # redirecting to the home page
        return redirect(url_for('edit'), code=302)


if __name__ == '__main__':
    app.run(debug=True)
