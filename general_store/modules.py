from general_store import app, bcrypt, login_manager
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy(app)

@login_manager.user_loader
def user_load(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  user_id = db.Column(db.Integer(), primary_key=True)
  user_name = db.Column(db.String(length=120), unique=False, nullable=False)
  email_address = db.Column(db.String(length=120), unique=True, nullable=False)
  password_hash = db.Column(db.String(length=120), unique=False, nullable=False)
  budget = db.Column(db.Integer(), default=1500, nullable=False)
  items = db.relationship("Item", backref="user_owned", lazy=True)

  def get_id(self):
        return self.user_id

  @property
  def password(self):
    return self.password
  @password.setter
  def password(self, simple_password):
    self.password_hash = bcrypt.generate_password_hash(simple_password).decode("utf-8")

  def check_password_correction(self, normal_password):
    return bcrypt.check_password_hash(self.password_hash, normal_password)

  
  def __repr__(self):
    return f"<{self.user_name}>"

class Item(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(length=120), unique=False, nullable=False)
  price = db.Column(db.Integer(), nullable=False)
  barcode = db.Column(db.Integer(), nullable=False)
  descriptrion = db.Column(db.String(length=1500), nullable=False)
  owner = db.Column(db.Integer(), db.ForeignKey("user.user_id"))

  def __repr__(self):
    return f"<{self.name}>"
  