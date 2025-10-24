import datetime
import dateutil.tz
import flask_login

from flask import Blueprint, render_template, request, redirect, url_for, flash


from . import model
from . import db

bp = Blueprint("main", __name__)


@bp.route("/")
@flask_login.login_required
def index():
    user_michael = model.User(email="michaelscott@gmail.com", name="Michael Scott")
    user_pam = model.User(email="pambeasley@gmail.com", name="Pam Beasley")
    posts = [
        model.Post(user=user_michael, text="This quote goes hard. Feel free to screenshot.", img="/imgs/quote.jpg", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())),
        model.Post(user=user_pam, text="Getting promoted to saleswoman",img="/imgs/meeting.jpg",timestamp=datetime.datetime.now(dateutil.tz.tzlocal())),
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
        text="My first post!",
        timestamp=datetime.datetime.now(dateutil.tz.tzlocal()),
        img="imgs/dwight_kitchen.jpg"
    )
    ]
    user.posts = posts
    return render_template("main/profile.html", posts=posts, user=user)

@bp.route("/post")
@flask_login.login_required
def test_post():
    user = model.User(id=2, email="dwightschrute@gmail.com", name="Dwight Schrute")    
    post = model.Post(
        id=4, user_id=user.id, text="This is me!", img="imgs/Dwight_Schrute.jpg", timestamp=datetime.datetime.now(dateutil.tz.tzlocal())
    )
    return render_template("main/post.html", post=post, user=user)

@bp.route("/new_post")
@flask_login.login_required
def new_post():
    return render_template("main/new_post.html")

@bp.route("/new_post" , methods=["POST"])
@flask_login.login_required
def new_post_publish():
    text = request.form.get("text")
    user = flask_login.current_user
    new_post = model.Post(text=text, user_id=user.id, timestamp=datetime.datetime.now(dateutil.tz.tzlocal()))
    db.session.add(new_post)
    db.session.commit()
    flash("Post published successfully!")
    return redirect(url_for("main.new_post", post_id=new_post.id))


