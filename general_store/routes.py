from general_store import app
from flask import render_template


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/market")
def market():
  data = [{
    "name": "pen",
    "price": 20,
    "barcode": 929929,
    "description": "pen description"
  }, {
    "name": "book",
    "price": 200,
    "barcode": 929000,
    "description": "book description"
  }, {
    "name": "pencil",
    "price": 10,
    "barcode": 999999,
    "description": "pencil description"
  }]
  return render_template("market.html", items=data)