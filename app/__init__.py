from flask import Flask
from config import Config # From congig.py import the Config class #
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .admin import admin
from flask_admin.contrib.sqla import ModelView
from .models import User, Post

app = Flask(__name__)
app.config.from_object(Config) # Tell Flask to read it and apply it #
db = SQLAlchemy(app) # use db Represent the database #
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Post,db.session))
