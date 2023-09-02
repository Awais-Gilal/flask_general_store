from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
  username = StringField(label="username")
  email = StringField(label="Email")
  password1 = PasswordField(label="Passowrd ")
  password2 = PasswordField(label="Passowrd ")
  submit = SubmitField(label="Submit")

