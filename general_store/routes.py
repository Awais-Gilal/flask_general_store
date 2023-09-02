from flask import render_template, url_for
from general_store import app
from general_store.modules import Item
from general_store.forms import RegisterForm


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/market")
def market():
  with app.app_context():
    data = Item.query.all()
  return render_template("market.html", items=data)

@app.route("/register")
def register():
  form = RegisterForm()
  return render_template("register.html", form=form)