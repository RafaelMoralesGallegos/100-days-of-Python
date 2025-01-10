from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! and Fuck you</p>"


@app.route("/bye")
def say_bye():
    return "<h1>Bye</h1>"


@app.route("/user/<username>/<int:years_old>")
def greet(username, years_old):
    return f"Hello {escape(username)}! you are {escape(years_old)}!"


if __name__ == "__main__":
    app.run(debug=True)
