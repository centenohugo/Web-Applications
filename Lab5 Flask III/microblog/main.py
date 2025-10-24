import datetime
import dateutil.tz
import flask_login

from flask import Blueprint, render_template, request, redirect, url_for, flash, abort


from . import model
from . import db

bp = Blueprint("main", __name__)


@bp.route("/")
@flask_login.login_required
def index():
    current_user_id = flask_login.current_user.id

    query = (
        db.select(model.Post)
        .where(model.Post.user_id != current_user_id) 
        .order_by(model.Post.timestamp.desc())
        .limit(10)
    )

    posts = db.session.execute(query).scalars().all()
    return render_template("main/index.html", posts=posts)


@bp.route("/profile/user/<int:user_id>")
@flask_login.login_required
def get_user(user_id):
    query = db.select(model.User).where(model.User.id == user_id)
    user = db.session.execute(query).scalar_one_or_none()
    if not user:
        abort(404, f"User with id {user_id} not found.")

    posts_query = db.select(model.Post).where(model.Post.user_id == user.id).order_by(model.Post.timestamp.desc())
    posts = db.session.execute(posts_query).scalars().all()

    return render_template("main/profile.html", user=user, posts=posts)

@bp.route("/post")
@flask_login.login_required
def test_post():
    user = flask_login.current_user    
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
    return redirect(url_for("main.post", post_id=new_post.id))


@bp.route("/view_published/<int:post_id>")
@flask_login.login_required
def post(post_id):
    post = db.session.get(model.Post, post_id)
    user = flask_login.current_user
    if not post:
        abort(404, "Post id {} doesn't exist.".format(post_id))
    return render_template("main/post.html", post=post, user=user)


