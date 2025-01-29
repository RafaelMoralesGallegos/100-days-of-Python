from flask import Flask
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
# with app.app_context():
#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)  # type: ignore
#     db.session.add(new_book)
#     db.session.commit()

# READ ALL RECORDS
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()

# READ SINGULAR
with app.app_context():
    book = db.session.execute(
        db.select(Book).where(Book.title == "Harry Potter")
    ).scalar()

# UPDATE A SINGLE
# with app.app_context():
#     boot_to_update = db.session.execute(
#         db.select(Book).where(Book.title == "Harry Potter")
#     ).scalar()
#     boot_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()

book_id = 1
with app.app_context():
    book_to_update = db.session.execute(
        db.select(Book).where(Book.id == book_id)
    ).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(
        db.select(Book).where(Book.id == book_id)
    ).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
