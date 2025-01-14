import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    blog_posts = get_blog()
    return render_template("index.html", posts=blog_posts)


def get_blog():
    try:
        response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return False
    else:
        data = response.json()
        return data


if __name__ == "__main__":
    app.run(debug=True)
