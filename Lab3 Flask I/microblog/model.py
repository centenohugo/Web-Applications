class Post:
    def __init__(self, post_id, user, text, img,  timestamp, comments = []):
        self.post_id = post_id
        self.user = user
        self.text = text
        self.img = img
        self.timestamp = timestamp
        self.comments = comments


class User:
    def __init__(self, user_id, email, name, profile_pic, posts = []):
        self.user_id = user_id
        self.email = email
        self.name = name
        self.posts = posts
        self.profile_pic = profile_pic
