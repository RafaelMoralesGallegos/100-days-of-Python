from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)


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
    new_book = Book(title=title, author=author, rating=rating)  # type: ignore
    db.session.add(new_book)
    db.session.commit()


@app.route("/")
def home():
    all_books = Book.query.order_by(Book.title)
    return render_template("index.html", all_books=all_books)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "GET":
        id = request.args.get("id")
        book = Book.query.filter_by(id=id).scalar()
        return render_template("edit.html", book=book)
    else:
        id = request.args.get("id")
        boot_to_update = Book.query.filter_by(id=id).scalar()
        boot_to_update.rating = request.form.get("rating")
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        create_new_book(
            request.form.get("title"),
            request.form.get("author"),
            request.form.get("rating"),
        )
        return redirect(url_for("home"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
