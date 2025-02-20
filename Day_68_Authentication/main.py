from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key-goes-here"


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()

# Create Flak-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def home():
    logged_in = current_user.is_authenticated
    return render_template("index.html", logged_in=logged_in)


@app.route("/register", methods=["GET", "POST"])
def register():
    logged_in = current_user.is_authenticated

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        hashed = generate_password_hash(request.form["password"])

        check_users = User.query.filter_by(email=email)
        if check_users:
            flash("Email already registered!!")
            return redirect(url_for("login"))

        else:
            new_user = User(email=email, password=hashed, name=name)  # type: ignore
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            logged_in = current_user.is_authenticated

            return render_template("secrets.html", name=name, logged_in=logged_in)

    return render_template("register.html", logged_in=logged_in)


@app.route("/login", methods=["GET", "POST"])
def login():
    logged_in = current_user.is_authenticated
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user:
            # Check hash
            if check_password_hash(user.password, password):
                login_user(user)
                logged_in = current_user.is_authenticated
                return render_template(
                    "secrets.html", name=user.name, logged_in=logged_in
                )
            else:
                flash("Wrong Password - Try again")
        else:
            flash("That user dosen't exist")

    return render_template("login.html", logged_in=logged_in)


@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html")


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    return send_from_directory("static", "files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
