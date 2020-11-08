from app import db

class Kifu(db.Model):

    __tablename__ = 'Kifu'
    __table_args__ = {'extend_existing': False}

    id = db.Column (
        db.Integer,
        primary_key = True
    )
    name = db.Column (
        db.String(64),
        index = False,
        unique = False,
        nullable = False
    )
    blackPlayer = db.Column (
        db.String(64),
        nullable = True,
    )
    whitePlayer = db.Column (
        db.String(64),
        nullable = True,
    )
    blackRank = None
    whiteRank = None
    result = ""