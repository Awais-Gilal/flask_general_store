from flask import Flask


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "a718e255ae1de2defcaf3be2"



from general_store import routes