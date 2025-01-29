from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)

all_books = []


##CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f"<Book {self.title}>"


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


# CREATE RECORD
def create_new_book(title, author, rating):
    with app.app_context():
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()


@app.route("/")
def home():
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        create_new_book(
            request.form.get("title"),
            request.form.get("author"),
            request.form.get("rating"),
        )
        return home()

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
