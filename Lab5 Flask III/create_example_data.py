from microblog import db, create_app, model
import datetime
import dateutil
app = create_app()
with app.app_context():
    user = model.User(email="mary@example.com", name="Mary", password="pwd")
    post = model.Post(user=user, text="First post")
    post2 = model.Post(user=user, text="Response post", response_to=post)
    post3 = model.Post(user=user, text="Response post 2", response_to=post)
    db.session.add(post2)
    db.session.add(post3)
    db.session.commit()