from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin # Apply login manager #
from app import db,app
from app import login
from hashlib import md5
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user




class User(UserMixin, db.Model):
    # Create four columns #
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def avatar(self, size): # Add avatar to one user #
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    # New user set the password #
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Check the password #
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username) 

class Post(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Mark = db.Column(db.Integer)
    Finish_Time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    Feedback = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.Mark)

# Loading a user from the database #
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class MyV1(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.username == "admin":
            return True
        return False
    can_create = False


admin=Admin(app)
admin.add_view(MyV1(User, db.session))
admin.add_view(MyV1(Post, db.session))