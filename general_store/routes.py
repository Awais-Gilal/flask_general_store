from general_store import app
from flask import render_template, jsonify, flash, redirect, url_for
from general_store.forms import RegisterForm, LoginForm
from general_store.modules import db, User, Item
from flask_login import login_user

@app.route("/")
def home_page():
  return render_template("index.html")

#market page
@app.route("/market")
def market_page():
  with app.app_context():
    items = Item.query.all()
  return render_template("market.html", items=items)

#register page
@app.route("/register", methods=["GET","POST"])
def register_page():
  form = RegisterForm()
  if form.validate_on_submit():
    data = User(user_name=form.user_name.data, email_address=form.email_address.data, password=form.password1.data)
    with app.app_context():
      db.session.add(data)
      db.session.commit()
    return redirect(url_for("market_page"))
  if form.errors != {}:
    if form.errors:
      for message in form.errors.values():
        flash(message, category="danger")
  return render_template("register.html", form=form)
  

@app.route("/login", methods=["GET", "POST"])
def login_page():
  form = LoginForm()
  if form.validate_on_submit():
    with app.app_context():
      attempted_user = User.query.filter_by(email_address=form.email_address.data).first()
    if attempted_user and attempted_user.check_password_correction(normal_password=form.password.data):
      login_user(attempted_user)
      flash(f"logined as {attempted_user.user_name}", category="danger")
      return redirect(url_for("market_page"))
    else:
      flash("invalid email or password")
  return render_template("login_page.html", form=form)



@app.route("/user")
def test_data():
  data = []
  with app.app_context():
    data_check = User.query.all()
  for d in data_check:
    data.append({
      "name":d.user_name,
      "email":d.email_address,
      "password":d.password_hash
    })
  return jsonify(data)