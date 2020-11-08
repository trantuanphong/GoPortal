from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gorankingportal.sqlite3'
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)
db.metadata.clear()

from .models import kifu
db.create_all()

from app import routes

app.run(debug=True)