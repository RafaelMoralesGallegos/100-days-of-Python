import requests
from flask import Flask, render_template

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/9fd727ea4ce5737d9ced")
response.raise_for_status()
data = response.json()


@app.route("/")
def get_home():
    return render_template("index.html", blog_posts=data)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
