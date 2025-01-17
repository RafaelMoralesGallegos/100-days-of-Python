import os
import smtplib as smtp

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

# *Email
load_dotenv()
my_email = os.environ.get("ULTRA_MAIL_MAIL")
password = os.environ.get("ULTRA_MAIL_PASS")


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


@app.route("/contact", methods=["POST", "GET"])
def get_contact():
    if request.method == "POST":
        data = request.form

        # Create the email body
        email_body = f"""
        Name: {data["name"]}
        Email: {data["email"]}
        Phone: {data["phone"]}
        Message: {data["message"]}
        """
        create_email(email_body)

        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html")


@app.route("/post/<int:id>")
def get_post(id):
    post = None
    for blog in data:
        if blog["id"] == id:
            post = blog
    return render_template("post.html", post=post)


def create_email(email_body):
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password=password)  # type: ignore
        connection.sendmail(
            from_addr=my_email,  # type: ignore
            to_addrs=my_email,  # type: ignore
            msg=f"Subject:New Contact Form Submission\n\n{email_body}",
        )


if __name__ == "__main__":
    app.run(debug=True)
