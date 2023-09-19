from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "3bc1f60a36a7eb52ea6f3851" #os.urandom(24).hex()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from general_store import routes