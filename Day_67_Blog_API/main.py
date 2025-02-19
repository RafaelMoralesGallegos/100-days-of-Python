from datetime import date, datetime

from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor, CKEditorField
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
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


with app.app_context():
    db.create_all()


@app.route("/")
def get_all_posts():
    """Create Home page of Blog Website

    Returns:
        HTML: index html in templates
    """
    all_posts = BlogPost.query.all()
    return render_template("index.html", all_posts=all_posts)


@app.route("/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)


class PostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Author's Name", validators=[DataRequired()])
    image = StringField(label="Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField(label="Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")


@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = PostForm()

    if form.validate_on_submit():
        today = datetime.today()
        date = f"{today.strftime('%B')} {today.day}, {today.year}"
        new_post = BlogPost(
            title=form.title.data,  # type: ignore
            subtitle=form.subtitle.data,  # type: ignore
            date=date,  # type: ignore
            body=form.body.data,  # type: ignore
            author=form.author.data,  # type: ignore
            img_url=form.image.data,  # type: ignore
        )
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form)


# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
