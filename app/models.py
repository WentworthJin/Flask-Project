from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin # Apply login manager #
from app import db,app
from app import login
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


class User(UserMixin, db.Model):
    # Create four columns #
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # New user set the password #
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Check the password #
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username) 

class Post(db.Model):
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

admin=Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))