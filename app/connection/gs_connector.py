from ..models.club import Club
from ..models.player import Player

import json, urllib, ssl

class GSheetConnector:

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    def loadClub():
        url = 'http://gsx2json.com/api?id=19dez-dGIocco9mUNAOaQ9fN7os9F8wRJyRVux7WEZ1g&sheet=1'
        uh = urllib.request.urlopen(url, context = GSheetConnector.ctx)
        rawData = uh.read()
        jsonData = json.loads(rawData)
        clubs = jsonData['rows']
        Club.insert(clubs)

    def loadMember():
        url = 'http://gsx2json.com/api?id=19dez-dGIocco9mUNAOaQ9fN7os9F8wRJyRVux7WEZ1g&sheet=2'
        uh = urllib.request.urlopen(url, context = GSheetConnector.ctx)
        rawData = uh.read()
        jsonData = json.loads(rawData)
        players = jsonData['rows']
        Player.insert(players)
