from app import app, db
from flask import request,jsonify, Flask
import json
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import pymongo
from bson.json_util import dumps
import json
import pandas as pd
from flask_jwt_extended import jwt_required, decode_token
from pyqrcode import QRCode
import pyqrcode
import png
import json


base_mongo_uri= "mongodb://new-user:Football123@cluster0-shard-00-00.aydzz.mongodb.net:27017,cluster0-shard-00-01.aydzz.mongodb.net:27017,cluster0-shard-00-02.aydzz.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-43ghe5-shard-0&authSource=admin&retryWrites=true&w=majority"
base_db = PyMongo(app, base_mongo_uri).db

@app.route("/college/register",methods=["POST"])
def registercollege():
    user_email = decode_token(request.headers["Access-Token"])['sub']['email']
    print(user_email)
    if(request.form):
        name = request.form['name']
        name = name.replace(" ","")
        mongo_uri= "mongodb://new-user:Football123@cluster0-shard-00-00.aydzz.mongodb.net:27017,cluster0-shard-00-01.aydzz.mongodb.net:27017,cluster0-shard-00-02.aydzz.mongodb.net:27017/" + name + "?ssl=true&replicaSet=atlas-43ghe5-shard-0&authSource=admin&retryWrites=true&w=majority"
        mongodb_client = PyMongo(app,mongo_uri)
        db = mongodb_client.db
        c_user = db.find_one({'college':name})
        if(c_user):
            return jsonify({'msg':'College Already Exist','Tip':'Try Using Full name of the college'})
        name = request.form['name']
        address = request.form['address']
        mobile = request.form['mobile']
        principal = request.form['principal']
        email = request.form['email']
        website = request.form['website']
    else:
        data = request.get_json()
        name = data["name"].replace(" ","")
        mongo_uri= "mongodb://new-user:Football123@cluster0-shard-00-00.aydzz.mongodb.net:27017,cluster0-shard-00-01.aydzz.mongodb.net:27017,cluster0-shard-00-02.aydzz.mongodb.net:27017/" + name + "?ssl=true&replicaSet=atlas-43ghe5-shard-0&authSource=admin&retryWrites=true&w=majority"
        mongodb_client = PyMongo(app,mongo_uri)
        db = mongodb_client.db
        name = data['name']
        address = data['address']
        mobile = data['mobile']
        principal = data['principal']
        email = data['email']
        website = data['website']
    url = "http://127.0.0.1:5000/app/college/" + name.replace(" ","")
    os.makedirs(os.path.join(app.instance_path, name.replace(" ","")), exist_ok=True)
    path = os.path.join(app.instance_path, name.replace(" ",""))
    qrcode = pyqrcode.create(url)
    qrcode.png(path + "/qrcode.png", scale = 6)
    try:
        college = db.details.find_one({'email':'email'})
        if(college):
            return jsonify({'msg':'College Already Exists'})
        else:
            db.details.insert_one({
                'name':name,
                'principal':principal,
                'website':website,
                'mobile':mobile,
                'address':address,
                'email':email,
                'path': path + "/qrcode.png"
            })
        user = base_db.users.find_one({'email':user_email,'college':""})
        if(user):
            base_db.users.update({
                'email': user_email
            },{
                'email':user['email'],
                'password': user['password'],
                'college': name.replace(" ",""),
            })
        else:
            return jsonify({'msg':'Cannot enter another college'})
        return jsonify({'message':'Registered Successfully'})
    except Exception as e:
        print(e)
        return jsonify({'message':'Something went wrong','error':e})
        
        

@app.route("/college/student", methods=["GET"])
def addStudentDetails():
    user_email = decode_token(request.headers["Access-Token"])['sub']['email']
    user = base_db.users.find_one({'email':user_email})
    name = user['college']
    mongo_uri= "mongodb://new-user:Football123@cluster0-shard-00-00.aydzz.mongodb.net:27017,cluster0-shard-00-01.aydzz.mongodb.net:27017,cluster0-shard-00-02.aydzz.mongodb.net:27017/" + name + "?ssl=true&replicaSet=atlas-43ghe5-shard-0&authSource=admin&retryWrites=true&w=majority"
    mongodb_client = PyMongo(app,mongo_uri)
    db = mongodb_client.db
    list_users = []
    registered_users = []
    
    # Student Data
    f = request.files["file"]
    if(f):
        f.save(os.path.join(app.instance_path, name.replace(" ",""), secure_filename(f.filename)))
        xl_file = pd.read_excel(os.path.join(app.instance_path, name, f.filename))
        list_users = []
        for row in xl_file.iterrows():
            user = row[1].to_dict()
            already_registered = db["users"].find_one({"Mobile":user["Mobile"]})
            if(already_registered):
                registered_users.append(user)
            else:
                user.update({'password':'password'})
                user.update({'Role':'Student'})
                list_users.append(user)
        try:
            if(len(list_users) > 0):
                db.users.insert_many(list_users) 
            if(len(registered_users) > 0):
                return jsonify({"already registered users" : registered_users })
            return jsonify({"sent" : "Correctly"})
        except Exception as e:
            print(e)
            return jsonify({'message':'Something went wrong','error':e})
                

@app.route("/college/staff", methods=["POST"])
def addStaffDetails():
    user_email = decode_token(request.headers["Access-Token"])['sub']['email']
    user = base_db.users.find_one({'email':user_email})
    name = user['college']
    mongo_uri= "mongodb://new-user:Football123@cluster0-shard-00-00.aydzz.mongodb.net:27017,cluster0-shard-00-01.aydzz.mongodb.net:27017,cluster0-shard-00-02.aydzz.mongodb.net:27017/" + name + "?ssl=true&replicaSet=atlas-43ghe5-shard-0&authSource=admin&retryWrites=true&w=majority"
    mongodb_client = PyMongo(app,mongo_uri)
    db = mongodb_client.db
    list_users = []
    registered_users = []
    
    # Student Data
    f = request.files["file"]
    if(f):
        f.save(os.path.join(app.instance_path, name.replace(" ",""), secure_filename(f.filename)))
        xl_file = pd.read_excel(os.path.join(app.instance_path, name, f.filename))
        list_users = []
        for row in xl_file.iterrows():
            user = row[1].to_dict()
            already_registered = db["users"].find_one({"Mobile":user["Mobile"]})
            if(already_registered):
                registered_users.append(user)
            else:
                user.update({'password':'password'})
                list_users.append(user)
        try:
            if(len(list_users) > 0):
                db.users.insert_many(list_users) 
            if(len(registered_users) > 0):
                return jsonify({"already registered users" : registered_users })
            return jsonify({"sent" : "Correctly"})
        except Exception as e:
            print(e)
            return jsonify({'message':'Something went wrong','error':e})
                
        
@app.route("/college/admin", methods=["GET"])
def adminDetails():
    user_email = decode_token(request.headers["Access-Token"])['sub']['email']
    user = base_db.users.find_one({'email':user_email})
    # user = list(user)
    name = user['college']
    mongo_uri= "mongodb://new-user:Football123@cluster0-shard-00-00.aydzz.mongodb.net:27017,cluster0-shard-00-01.aydzz.mongodb.net:27017,cluster0-shard-00-02.aydzz.mongodb.net:27017/" + name + "?ssl=true&replicaSet=atlas-43ghe5-shard-0&authSource=admin&retryWrites=true&w=majority"
    mongodb_client = PyMongo(app,mongo_uri)
    db = mongodb_client.db
    details = list(db.details.find({}))[0]
    return jsonify({'name':details['name'],'principal':details["principal"],'website':details["website"],'mobile':details["mobile"],'address':details["address"]})