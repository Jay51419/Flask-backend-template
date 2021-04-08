from flask import Flask, jsonify
from flask_pymongo import PyMongo
import os

import json
from bson import ObjectId
app = Flask(__name__)

mongo_uri= "mongodb+srv://jay:jay51419@cluster0.xmpnk.mongodb.net/Auth?retryWrites=true&w=majority"
mongodb_client = PyMongo(app,mongo_uri)
db = mongodb_client.db


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
folders = []

for root,dirs,files in os.walk(os.path.dirname(os.path.abspath(__file__))):
	folders.extend(dirs)
print()

__all__= list(filter(("__pycache__").__ne__, folders))
from . import *

@app.route("/")
def get_users():
	return JSONEncoder().encode(db.users.find_one()) 