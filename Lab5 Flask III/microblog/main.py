import datetime
import dateutil.tz
import flask_login

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
@flask_login.login_required
def index():
    user = model.User(email="mary@example.com", name="mary")
    posts = [
        model.Post(user=user, text="Test post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())),
        model.Post(user=user, text="Another post", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())),
    ]
    return render_template("main/index.html", posts=posts)

@bp.route("/profile")
@flask_login.login_required
def test_user():
    user = model.User(
    id=2,
    email="dwightschrute@gmail.com",
    name="Dwight Schrute",
    password="password"
    )  
    posts = [
    model.Post(
        user_id=1,
        text="¡Primer post de prueba!",
        timestamp=datetime.datetime.now(dateutil.tz.tzlocal()),
    ),
    model.Post(
        user_id=2,
        text="Respuesta al primer post",
        timestamp=datetime.datetime.now(dateutil.tz.tzlocal()),
    )
    ]
    user.posts = posts
    return render_template("main/profile.html", posts=posts, user=user)

@bp.route("/post")
@flask_login.login_required
def test_post():
    user = model.User(2, "dwightschrute@gmail.com", "Dwight Schrute","imgs/profilepic.jpg")    
    post = model.Post(
        4, user, "This is me!", "imgs/Dwight_Schrute.jpg", datetime.datetime.now(dateutil.tz.tzlocal()),
        comments = [
            "Great photo!",
            "I like your shirt.",
            "Where is this taken?"
        ]
    )
    return render_template("main/post.html", post=post, user=user)

