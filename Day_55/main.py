from flask import Flask
from markupsafe import escape

app = Flask(__name__)


def make_bold(function):
    def wrapping_function():
        return f"<b>{function()}</b>"

    return wrapping_function


def make_emphasis(function):
    def wrapping_function():
        return f"<em>{function()}</em>"

    return wrapping_function


def make_underlined(function):
    def wrapping_function():
        return f"<u>{function()}</u>"

    return wrapping_function


@app.route("/")
def hello_world():
    return (
        "<h1 style='text-align: center'>Hello, World! and Fuck you</h1>"
        "<p>this is text</p>"
        '<img src="https://media0.giphy.com/media/kYNVwkyB3jkauFJrZA/giphy.webp?cid=790b7611p10rqzus34tbrbah720d7b4khy18rsr37ha4632r&ep=v1_gifs_trending&rid=giphy.webp&ct=g">'
    )


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"


@app.route("/user/<username>/<int:years_old>")
def greet(username, years_old):
    return f"Hello {escape(username)}! you are {escape(years_old)}!"


if __name__ == "__main__":
    app.run(debug=True)
