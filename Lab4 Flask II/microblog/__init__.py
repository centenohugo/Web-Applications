from flask import Flask

# Things to import at the beginning
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Declarations to insert before the create_app function:
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

def create_app(test_config=None):
    app = Flask(__name__)

    # A secret for signing session cookies
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://microblog:waDBlog@localhost/Microblog"
    app.config['SECRET_KEY'] = 'waDBlog'
    db.init_app(app)

    # Register blueprints
    # (we import main from here to avoid circular imports in the next lab)
    from . import main
    from . import auth

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    return app
