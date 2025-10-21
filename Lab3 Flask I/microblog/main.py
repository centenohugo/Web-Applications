import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user = model.User(1, "mary@example.com", "Michael", "imgs/profilepic.jpg")
    posts = [
        model.Post(
            1, user, "Meeting with the team. Went faster than expected! (that's what she said)", "imgs/meeting.jpg", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Post(
            2, user, "This quote goes hard, feel free to repost.", "imgs/quote.jpg", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Post(
            3, user, "It's Britney..!","imgs/profilepic.jpg", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("main/index.html", posts=posts)

@bp.route("/profile")
def test_user():
    user = model.User(2, "dwightschrute@gmail.com", "Dwight Schrute","imgs/profilepic.jpg")    
    posts = [
    model.Post(
        4, user, "This is me!", "imgs/Dwight_Schrute.jpg", datetime.datetime.now(dateutil.tz.tzlocal())
    ),
    model.Post(
        5, user, "I am hungry.", "imgs/dwight_kitchen.jpg", datetime.datetime.now(dateutil.tz.tzlocal()))
    ]
    user.posts = posts
    return render_template("main/profile.html", posts=posts, user=user)

@bp.route("/post")
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

