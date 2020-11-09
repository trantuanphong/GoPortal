from app import app, db
from flask import render_template, request
from .connection import kgs_connecter as Kgs
from .models.club import Club

import json, urllib, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

@app.route("/")
@app.route("/clubs", methods = ["GET"])
def getClubs():
    url = 'http://gsx2json.com/api?id=19dez-dGIocco9mUNAOaQ9fN7os9F8wRJyRVux7WEZ1g&sheet=1'
    uh = urllib.request.urlopen(url, context = ctx)
    rawData = uh.read()
    jsonData = json.loads(rawData)
    clubs = jsonData['rows']
    return render_template('clubs.html', clubs = clubs)

@app.route("/clubs", methods = ["POST"])
def addClubs():
    data = request.get_json(force = True)
    Club.insert(data)
    message = "Insert successfully!"
    response = app.response_class(
        response=json.dumps(message),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/clubs", methods = ["PUT"])
def editClubs():
    data = request.get_json(force = True)
    Club.update(data)
    message = "Update successfully!"
    response = app.response_class(
        response=json.dumps(message),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/clubs", methods = ["DELETE"])
def deleteClubs():
    data = request.get_json(force = True)
    Club.delete(data)
    message = "Delete successfully!"
    response = app.response_class(
        response=json.dumps(message),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/club/<id>", methods = ["GET"])
def getClub(id):
    url = 'http://gsx2json.com/api?id=19dez-dGIocco9mUNAOaQ9fN7os9F8wRJyRVux7WEZ1g&sheet=1&q=' + id
    uh = urllib.request.urlopen(url, context = ctx)
    rawData = uh.read()
    jsonData = json.loads(rawData)
    clubs = jsonData['rows']
    club = clubs[0]
    return render_template('club.html', club = club)

@app.route("/players", methods = ["GET"])
def getPlayers():
    url = 'http://gsx2json.com/api?id=19dez-dGIocco9mUNAOaQ9fN7os9F8wRJyRVux7WEZ1g&sheet=2'
    uh = urllib.request.urlopen(url, context = ctx)
    rawData = uh.read()
    jsonData = json.loads(rawData)
    players = jsonData['rows']
    return render_template('players.html', players = players)

@app.route("/players", methods = ["POST"])
def addPlayers():
    return "123"

@app.route("/players", methods = ["PUT"])
def editPlayers():
    return "123"

@app.route("/players", methods = ["DELETE"])
def deletePlayers():
    return "123"

@app.route("/player/<id>")
def getPlayer(id):
    player = Kgs.getUserInfo(id)
    return render_template('player.html', player = player)