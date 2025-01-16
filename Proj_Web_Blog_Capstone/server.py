from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template("index.html", page="home")


@app.route("/about")
def get_about():
    return render_template("about.html", page="about")


@app.route("/contact")
def get_contact():
    return render_template("contact.html", page="contact")


if __name__ == "__main__":
    app.run(debug=True)
