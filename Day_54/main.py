from flask import Flask

app = Flask(__name__)


@app.route("/")  # ?The syntax is a Python Decorator
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
