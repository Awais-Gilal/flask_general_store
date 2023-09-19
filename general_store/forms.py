from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo, Email, Length, DataRequired, ValidationError
from general_store.modules import User

class RegisterForm(FlaskForm):

  def validate_email_address(self, field):
    data_to_chech = User.query.filter_by(email_address=field.data).first()
    if data_to_chech:
      raise ValidationError("Email already exists")

  user_name = StringField(label="User name", validators=[Length(max=50, min=5), DataRequired()])
  email_address = StringField(label="Email", validators=[Length(max=60, min=11), Email(), DataRequired()])
  password1 = PasswordField(label="Password", validators=[Length(min=5), DataRequired()])
  password2 = PasswordField(label="Conform Passowrd", validators=[Length(min=5), EqualTo("password1"), DataRequired()])
  submit = SubmitField(label="Submit")

class LoginForm(FlaskForm):
  email_address = StringField(label="Email Address", validators=[DataRequired(), Email(), Length(min=11, max=60)])
  password = PasswordField(label="Password", validators=[DataRequired(), Length(min=5)])
  submit = SubmitField(label="Login")