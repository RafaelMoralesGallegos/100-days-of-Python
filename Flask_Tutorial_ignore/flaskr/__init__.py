import os

from flask import Flask


def create_app(test_config=None) -> Flask:
    """Creation of webpage using Flask framework

    Args:
        test_config (_type_, optional): If testing web page. Defaults to None.

    Returns:
        Flask: main application using flask
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config is None:
        # Load test config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # Load test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # Import databse form db file
    from . import db

    db.init_app(app)

    # Create blueprint for authorization
    from . import auth

    app.register_blueprint(auth.bp)

    return app


def main():
    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
