from flask import Flask
from config import Config # From congig.py import the Config class #

app = Flask(__name__)
app.config.from_object(Config) # Tell Flask to read it and apply it #

from app import routes