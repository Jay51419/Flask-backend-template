from app import app, db
from flask import request,jsonify, Flask
from flask_pymongo import PyMongo


@app.route('/app/college/<name>', methods = ["GET"])
def addApp5College(name):
    mongo_uri= "mongodb://new-user:Football123@cluster0-shard-00-00.aydzz.mongodb.net:27017,cluster0-shard-00-01.aydzz.mongodb.net:27017,cluster0-shard-00-02.aydzz.mongodb.net:27017/" + name + "?ssl=true&replicaSet=atlas-43ghe5-shard-0&authSource=admin&retryWrites=true&w=majority"
    mongodb_client = PyMongo(app,mongo_uri)
    colg_db = mongodb_client.db
    details = list(colg_db.details.find({}))
    name = details[0]['name']
    return jsonify({'name': name})

