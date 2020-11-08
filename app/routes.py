from app import app, db
from flask import render_template
from .models.kifu import Kifu
from .connection import kgs_connecter as Kgs

import json, urllib, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/ranking")
@app.route("/ranking/")
@app.route("/ranking/<category>")
def getRanking(category = None):
    if category is None:
        result = ['Nothing']
    else:
        result = ['P1', 'P2', 'P3']
    return render_template('ranking.html', players = result)

@app.route("/players")
def getPlayers():
    url = 'http://gsx2json.com/api?id=19dez-dGIocco9mUNAOaQ9fN7os9F8wRJyRVux7WEZ1g&sheet=2'
    uh = urllib.request.urlopen(url, context = ctx)
    rawData = uh.read()
    jsonData = json.loads(rawData)
    players = jsonData['rows']
    return render_template('players.html', players = players)

@app.route("/player/<id>")
def getPlayer(id):
    player = Kgs.getUserInfo(id)
    return render_template('player.html', player = player)

@app.route("/kifus")
def getKifus():
    kifus = []
    kifus.append(Kifu())
    kifus.append(Kifu())
    kifu = Kifu (
        name = 'Test'
    )
    db.session.add(kifu)
    db.session.commit()
    return render_template('kifus.html', kifus = kifus)

@app.route("/kifu/<id>")
def getKifu(id):
    kifu = Kifu()
    return  render_template('kifu.html', kifu = kifu)

@app.route("/clubs")
def getClubs():
    url = 'http://gsx2json.com/api?id=19dez-dGIocco9mUNAOaQ9fN7os9F8wRJyRVux7WEZ1g&sheet=1'
    uh = urllib.request.urlopen(url, context = ctx)
    rawData = uh.read()
    jsonData = json.loads(rawData)
    clubs = jsonData['rows']
    return render_template('clubs.html', clubs = clubs)

@app.route("/club/<id>")
def getClub(id):
    url = 'http://gsx2json.com/api?id=19dez-dGIocco9mUNAOaQ9fN7os9F8wRJyRVux7WEZ1g&sheet=1&q=' + id
    uh = urllib.request.urlopen(url, context = ctx)
    rawData = uh.read()
    jsonData = json.loads(rawData)
    clubs = jsonData['rows']
    club = clubs[0]
    return render_template('club.html', club = club)