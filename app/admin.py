from flask_admin import Admin
import app
from flask import Blueprint, render_template

admin=Admin(app, name="Admin System")


