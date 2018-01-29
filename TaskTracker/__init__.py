from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
app.config['SECRET_KEY'] = "my-secret-key"
db = SQLAlchemy(app)

from TaskTracker import routes, models
