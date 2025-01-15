import requests
from flask import Flask, render_template

from post import Post

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
data = response.json()
blog_posts = []

for blog in data:
    new_blog = Post(blog)
    blog_posts.append(new_blog)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)


@app.route("/post/<int:id>")
def get_post(id):
    request = None
    for blog in blog_posts:
        if blog.id == id:
            request = blog
    return render_template("post.html", request=request)


if __name__ == "__main__":
    app.run(debug=True)
