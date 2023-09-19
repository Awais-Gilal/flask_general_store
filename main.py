from general_store import app
from general_store.modules import db
import os
file = "instance/database.db"
if not os.path.exists(file):
  with app.app_context():
    db.create_all()
  

if __name__ == "__main__":
  app.run(port=81, host='0.0.0.0')
