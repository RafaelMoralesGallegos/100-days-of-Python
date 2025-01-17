from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def get_login():
    user_data = {
        "username": request.form["username"],
        "password": request.form["password"],
    }
    return render_template("login.html", user_data=user_data)


if __name__ == "__main__":
    app.run(debug=True)
