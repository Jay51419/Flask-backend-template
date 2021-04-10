from app import app, db
from flask import request,jsonify, Flask
import json
from flask_pymongo import PyMongo
import os
import pymongo
import json


@app.route("/college/register",methods=["POST"])
def registercollege():
    if(request.form):
        return jsonify({"sent" : "Correctly"})
    else:
        data = request.get_json()
        name = data["name"].replace(" ","")
        mongo_uri= "mongodb://new-user:Football123@cluster0-shard-00-00.aydzz.mongodb.net:27017,cluster0-shard-00-01.aydzz.mongodb.net:27017,cluster0-shard-00-02.aydzz.mongodb.net:27017/" + name + "?ssl=true&replicaSet=atlas-43ghe5-shard-0&authSource=admin&retryWrites=true&w=majority"
        mongodb_client = PyMongo(app,mongo_uri)
        db = mongodb_client.db
        try:
            db.users.insert_one({"email":data["email"],"password":data["password"]})
            return jsonify({"message":"Registeration successful"})
        except Exception as e:
            print(e)
            return jsonify({"message":"Something went wrong while registering"})