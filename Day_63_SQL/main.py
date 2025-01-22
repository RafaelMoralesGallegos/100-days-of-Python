from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

all_books = []


@app.route("/")
def home():
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        all_books.append(
            {
                "title": request.form.get("title"),
                "author": request.form.get("author"),
                "rating": request.form.get("rating"),
            }
        )
        return home()

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
