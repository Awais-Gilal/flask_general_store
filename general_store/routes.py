from flask import render_template, url_for, jsonify, redirect, flash
from general_store import app
from general_store.modules import Item, User, db
from general_store.forms import RegisterForm


@app.route("/")
def home_page():
  return render_template("index.html")


@app.route("/market")
def market_page():
  with app.app_context():
    data = Item.query.all()
  return render_template("market.html", items=data)


@app.route("/register", methods=["GET", "POST"])
def register_page():
  form = RegisterForm()
  if form.validate_on_submit():
    data_to_submit = User(user=form.username.data,
                          email=form.email.data,
                          password=form.password1.data)
    with app.app_context():
      db.session.add(data_to_submit)
      db.session.commit()
    return redirect(url_for('market_page'))
  if form.errors:
    for error in form.errors.values():
      flash(error, category="danger")
  return render_template("register.html", form=form)








@app.route("/user")
def user_test():
  data = []
  with app.app_context():
    d = User.query.all()
    for v in d:
      data.append({"name": v.user, "email": v.email})
  return jsonify(data)


@app.route("/item")
def item_test():
  data = []
  with app.app_context():
    d = Item.query.all()
    for v in d:
      data.append({"name": v.name, "price": v.price})
  return jsonify(data)