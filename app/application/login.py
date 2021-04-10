from app import app, db
from flask import request,jsonify, Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import create_access_token


@app.route('/app/login/<name>', methods = ["POST"])
def selectCollege(name):
    data = request.get_json()
    mongo_uri= "mongodb://new-user:Football123@cluster0-shard-00-00.aydzz.mongodb.net:27017,cluster0-shard-00-01.aydzz.mongodb.net:27017,cluster0-shard-00-02.aydzz.mongodb.net:27017/" + name + "?ssl=true&replicaSet=atlas-43ghe5-shard-0&authSource=admin&retryWrites=true&w=majority"
    mongodb_client = PyMongo(app,mongo_uri)
    colg_db = mongodb_client.db
    user = colg_db.users.find_one({'Mobile':data['mobile']})
    try:
        if(user):
            token = create_access_token(identity=data, fresh= True)
            if(user['password'] == data["password"]):
                return jsonify({"message":"Login successful","token":token})
            else:
                return jsonify({"message":"Incorrect password"})
        else:
            return jsonify({"message":"User not found with this email."}) 
    except Exception as e:
        print(e)
        return jsonify({"message":"Something went wrong while logging in"})
        
        
        

    