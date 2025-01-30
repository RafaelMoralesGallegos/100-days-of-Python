import requests
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

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
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250))

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
    all_movies = Movie.query.order_by(Movie.ranking)
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
        print(title)

        return redirect(url_for("home"))

    return render_template("add.html", form=form)


# *Methods

if __name__ == "__main__":
    app.run(debug=True)
