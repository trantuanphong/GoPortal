from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GoPortal.sqlite3'
db = SQLAlchemy(app)

from .models.club import Club
from .models.player import Player
db.drop_all()
db.create_all()

from .connection.gs_connector import GSheetConnector
GSheetConnector.loadClub()
GSheetConnector.loadMember()

from app import routes

app.run(debug=True)