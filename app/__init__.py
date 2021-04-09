from flask import Flask, jsonify
from flask_pymongo import PyMongo
import os
import pymongo

import json
from bson import ObjectId
app = Flask(__name__)

mongo_uri= "mongodb://new-user:Football123@cluster0-shard-00-00.aydzz.mongodb.net:27017,cluster0-shard-00-01.aydzz.mongodb.net:27017,cluster0-shard-00-02.aydzz.mongodb.net:27017/DJ?ssl=true&replicaSet=atlas-43ghe5-shard-0&authSource=admin&retryWrites=true&w=majority"
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


