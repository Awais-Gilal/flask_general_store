from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import  Length, EqualTo, Email, DataRequired, ValidationError
from general_store.modules import User

class RegisterForm(FlaskForm):
  def validate_email(self, field):
    email_address = User.query.filter_by(email=field.data).first()
    if email_address:
      raise ValidationError('Email address already exists! ')
  
  username = StringField(label="username", validators=[Length(min=3, max=50), DataRequired()])
  email = StringField(label="Email" ,validators=[Length(min=10), Email(), DataRequired() ])
  password1 = PasswordField(label="Passowrd", validators=[Length(min=5), DataRequired()])
  password2 = PasswordField(label="Passowrd", validators=[Length(min=5), DataRequired(), EqualTo('password1')])
  submit = SubmitField(label="Submit")

