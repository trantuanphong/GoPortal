from app import db

class Club(db.Model):

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    province = db.Column(db.String(50), unique = False, nullable = False)
    address = db.Column(db.String(500), unique = False, nullable = False)
    contact = db.Column(db.String(120), unique = False, nullable = False)
    lng = db.Column(db.Float, unique = False, nullable = False)
    lat = db.Column(db.Float, unique = False, nullable = False)

    members = db.relationship('Player', lazy = 'select', backref=db.backref('person', lazy='joined'))

    def init(obj):
        club = Club()
        if 'id' in obj:
            club.id = obj.get('id')
        club.name = obj.get('name', '')
        club.province = obj.get('province', '')
        club.address = obj.get('address', '')
        club.contact = obj.get('contact', '')
        club.lng = obj.get('lng', 0)
        club.lat = obj.get('lat', 0)

        return club

    def insert(clubs):
        for club in clubs:
            db.session.add(Club.init(club))
        db.session.commit()
    
    def update(clubs):
        for club in clubs:
            Club.query.filter_by(id = club.get('id')).update(club)
        db.session.commit()
    
    def delete(clubs):
        for club in clubs:
            Club.query.filter_by(id = club.get('id')).delete()
        db.session.commit()