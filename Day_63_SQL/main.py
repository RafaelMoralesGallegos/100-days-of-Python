from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

all_books = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        print(True)

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
