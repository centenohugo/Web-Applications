from microblog import db, create_app, model
app = create_app()
with app.app_context():
    query = db.select(model.Post)
    posts = db.session.execute(query).scalars().all()
    print(posts[0].text)
    print(posts[1].text)
    print(posts[1].response_to.text)
    print(posts[0].user.email)
    print(len(posts[0].responses))
    print(posts[0].responses[0].text)