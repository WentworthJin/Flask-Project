import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Add cryptographic key #
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Hardest-Password-in-world'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False