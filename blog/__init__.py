from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_basicauth import BasicAuth


db = SQLAlchemy()
basic_auth = BasicAuth()
admin = Admin(name='waydk blog', template_mode='bootstrap4')


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    admin.init_app(app)
    basic_auth.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models
        return app
