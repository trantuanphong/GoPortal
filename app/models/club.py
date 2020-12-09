from app import db

class Club(db.Model):

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    province = db.Column(db.String(50), unique = False, nullable = False)
    address = db.Column(db.String(500), unique = False, nullable = False)
    contact = db.Column(db.String(120), unique = False, nullable = False)
    lng = db.Column(db.Float, unique = False, nullable = False)
    lat = db.Column(db.Float, unique = False, nullable = False)

    members = db.relationship('Player', lazy = 'select') #, backref=db.backref('members', lazy='joined'))

    def __init__(self):
        self.lng = 105.6207275390417
        self.lat = 21.281789604927425

    def init(obj):
        club = Club()
        if 'id' in obj:
            club.id = obj.get('id')
        club.name = obj.get('Name', '')
        club.province = obj.get('Province', '')
        club.address = obj.get('Address', '')
        club.contact = obj.get('Contact', '')
        club.lng = obj.get('Lng', 105.6207275390417)
        club.lat = obj.get('Lat', 21.281789604927425)

        return club

    def insert(clubs):
        for club in clubs:
            db.session.add(Club.init(club))
        db.session.commit()
    
    def update(id, club):
        Club.query.filter_by(id = id).update(club)
        db.session.commit()
    
    def delete(id):
        Club.query.filter_by(id = id).delete()
        db.session.commit()

    def getById(id):
        return Club.query.filter_by(id = id).first()

    def getAll():
        return Club.query.all()

    def dumpHTML(self):
        info = '<strong><a href="/club/'+str(self.id)+'">'+ self.name +'</a></strong>'
        info += '<p>Contact: '+ self.contact +'</p>'
        return info