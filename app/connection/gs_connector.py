from ..models.club import Club
from ..models.player import Player

import json, urllib, ssl

class GSheetConnector:

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    def loadClub():
        url = 'https://sheet2api.com/v1/3UU1EL2CRVKP/danh-sach-cac-clb/club'
        uh = urllib.request.urlopen(url, context = GSheetConnector.ctx)
        rawData = uh.read()
        jsonData = json.loads(rawData)
        clubs = jsonData
        Club.insert(clubs)

    def loadMember():
        url = 'https://sheet2api.com/v1/3UU1EL2CRVKP/danh-sach-cac-clb/member'
        uh = urllib.request.urlopen(url, context = GSheetConnector.ctx)
        rawData = uh.read()
        jsonData = json.loads(rawData)
        players = jsonData
        Player.insert(players)
