from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    rank = db.Column(db.String(3), nullable = False)
    hometown = db.Column(db.String(20))
    birthYear = db.Column(db.Integer)

    clubId = db.Column(db.Integer, db.ForeignKey('club.id'), nullable = False)

    def init(obj):
        player = Player()
        player.name = obj.get('name')
        player.rank = obj.get('rank','?')
        player.hometown = obj.get('hometown')
        player.birthYear = obj.get('birthyear')
        player.clubId = obj.get('clubid')
        return player

    def insert(players):
        for player in players:
            db.session.add(Player.init(player))
        db.session.commit()    