import os

import requests
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

load_dotenv()
THE_MOVIE_DB_API = os.environ.get("THE_MOVIE_DB_API")

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

# *Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# *Classes
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f"<Movie {self.title}>"


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g 5.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class MovieAdd(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


with app.app_context():
    db.create_all()


# *Apps
@app.route("/")
def home():
    """Main Page of app"""
    all_movies = Movie.query.order_by(Movie.rating.desc())
    movie_list = all_movies.all()
    for i, movie in enumerate(movie_list):
        get_movie_ranking(movie, i)

    return render_template("index.html", all_movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """Edit the rating and review of a single card/movie"""
    id = request.args.get("id")
    movie = Movie.query.filter_by(id=id).scalar()
    form = RateMovieForm()

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    id = request.args.get("id")
    Movie.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieAdd()
    if form.validate_on_submit():
        title = form.title.data
        results = get_movie_list(title)

        return render_template("select.html", results=results)

    return render_template("add.html", form=form)


@app.route("/select")
def select():
    movie_id = request.args.get("id")
    result = get_movie_data(movie_id)
    secure_base_url = "https://image.tmdb.org/t/p/w500"
    new_movie = create_new_movie(
        result.get("title"),
        int(result.get("release_date")[:4]),
        result.get("overview"),
        f"{secure_base_url}{result.get("poster_path")}",
    )

    return redirect(url_for("edit", id=new_movie.id))


# *Methods
def get_movie_list(title):
    url = f"https://api.themoviedb.org/3/search/movie?query={title}&language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {THE_MOVIE_DB_API}",
    }

    response = requests.get(url, headers=headers).json()
    return response["results"]


def get_movie_data(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {THE_MOVIE_DB_API}",
    }

    response = requests.get(url, headers=headers).json()
    return response


def create_new_movie(title, year, description, img_url):
    """Add new movie to db"""
    new_movie = Movie(title=title, year=year, description=description, img_url=img_url)  # type: ignore
    db.session.add(new_movie)
    db.session.commit()

    return new_movie


def get_movie_ranking(movie, ranking: int):
    """Update movie ranking according to main file"""
    movie.ranking = ranking + 1
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
