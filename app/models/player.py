from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique = False, nullable = False)
    rank = db.Column(db.String(3), unique = False, nullable = False)
    clubId = db.Column(db.Integer, db.ForeignKey('club.id'), nullable = False)