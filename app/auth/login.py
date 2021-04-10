from app import app,db,check_password
from flask import request,jsonify
from flask_jwt_extended import create_access_token

@app.route("/login",methods=['POST'])
def login():
	data = request.get_json()
	print(data)
	try:
		user = db["users"].find_one({"email":data["email"]})
		print(user)
		if user:
			token = create_access_token(identity=data, fresh= True)
			return jsonify({"message":"Login successful","token":token}) if check_password(data["password"].encode('utf-8'),user["password"]) else jsonify({"message":"Incorrect password"})
		else:
			return jsonify({"message":"User not found with this email."}) 
	except Exception as e:
		print(e)
		return jsonify({"message":"Something went wrong while logging in"})