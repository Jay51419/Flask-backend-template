from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
import os
import pymongo
import bcrypt
import json
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
mongo_uri= "mongodb://new-user:Football123@cluster0-shard-00-00.aydzz.mongodb.net:27017,cluster0-shard-00-01.aydzz.mongodb.net:27017,cluster0-shard-00-02.aydzz.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-43ghe5-shard-0&authSource=admin&retryWrites=true&w=majority"
mongodb_client = PyMongo(app,mongo_uri)
db = mongodb_client.db
app.config["JWT_TOKEN_LOCATION"] = ["headers"]

# If true this will only allow the cookies that contain your JWTs to be sent
# over https. In production, this should always be set to True
app.config["JWT_COOKIE_SECURE"] = False


app.config["JWT_SECRET_KEY"] = "super-secret"
# Change this in your code!
jwt = JWTManager(app)
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
    

def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt(16))

def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)
    
folders = []

for root,dirs,files in os.walk(os.path.dirname(os.path.abspath(__file__))):
	folders.extend(dirs)
print()

__all__= list(filter(("__pycache__").__ne__, folders))
from . import *


