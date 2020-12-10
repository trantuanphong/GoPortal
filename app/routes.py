from app import app, db
from flask import render_template, request, make_response
from .connection import kgs_connecter as Kgs
from .utils.map_util import MapboxUtil
from .models.club import Club
from .models.player import Player
from .iefile.csv_rw import CSVHandler

import json, urllib, ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

@app.route("/")
@app.route("/clubs", methods = ["GET"])
def getClubs():
    clubs = Club.getAll()
    datasource = MapboxUtil.toGeoJSON(clubs)
    return render_template('clubs.html', clubs = clubs, datasource = datasource)

@app.route("/clubs/download")
def dowloadClubs():
    clubs = Club.getAll()
    output = make_response(CSVHandler.exportClub(clubs))
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv; charset=UTF-8"
    return output

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

@app.route("/club/<id>", methods = ["PUT"])
def editClub(id):
    data = request.get_json(force = True)
    Club.update(id, data)
    message = "Update successfully!"
    response = app.response_class(
        response=json.dumps(message),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/club/<id>", methods = ["DELETE"])
def deleteClub(id):
    Club.delete(id)
    message = "Delete successfully!"
    response = app.response_class(
        response=json.dumps(message),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/club", methods = ["GET"])
@app.route("/club/<id>", methods = ["GET"])
def getClub(id = None):
    club = Club()
    if id is not None:
        club = Club.getById(id)
    return render_template('club.html', club = club)

@app.route("/club/<id>/download")
def downloadClubMember(id):
    club = Club.getById(id)
    members = club.members

    output = make_response(CSVHandler.exportClubMember(members))
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output

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
    data = request.get_json(force = True)
    Player.insert(data)
    message = "Insert successfully!"
    response = app.response_class(
        response=json.dumps(message),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/player/<id>", methods = ["PUT"])
def editPlayer(id):
    data = request.get_json(force = True)
    Player.update(id, data)
    message = "Update successfully!"
    response = app.response_class(
        response=json.dumps(message),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/player/<id>", methods = ["DELETE"])
def deletePlayer(id):
    Player.delete(id)
    message = "Delete successfully!"
    response = app.response_class(
        response=json.dumps(message),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/player")
@app.route("/player/<id>")
def getPlayer(id = None):
    # player = Kgs.getUserInfo(id)
    player = {}
    if id is not None:
        player = Player.getById(id)
    clubs = Club.getAll()
    return render_template('player.html', player = player, clubs = clubs)

@app.route("/player/<id>/kgs")
def getKgsInfo(id):
    player = Player.getById(id)
    kgs = Kgs.getUserInfo(player.kgs)
    return render_template('kgs.html', kgs = kgs, player = player)