from general_store import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  user = db.Column(db.String(length=250), nullable=False, unique=False)
  email = db.Column(db.String(length=250), nullable=False, unique=True)
  password = db.Column(db.String(length=60), nullable=True, unique=False)
  Budget = db.Column(db.Integer(), default=1000, nullable=False)
  items = db.relationship("Item", backref="user_owned", lazy=True)
  def __repr__(self):
    return f"< Id {self.id} >"



class Item(db.Model):
  id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True)
  name = db.Column(db.String(length=60), nullable=False)
  price = db.Column(db.Integer(), nullable=False)
  barcode = db.Column(db.Integer(), unique=True, nullable= False)
  description = db.Column(db.String(length=1024), nullable=False)
  owner = db.Column(db.Integer(), db.ForeignKey("user.id"))
  def __repr__(self):
    return f"< Item {self.name} >"

