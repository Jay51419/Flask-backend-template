from app import app,db
from flask import request,jsonify


@app.route("/login",methods=['POST'])
def login():
	data = request.get_json()
	print(data)
	try:
		user = db["users"].find_one({"email":data["email"]})
		print(user)
		if user:
			return jsonify({"message":"Login successful"}) if data["password"] == user["password"] else jsonify({"message":"Incorrect password"})
		else:
			return jsonify({"message":"User not found with this email."}) 
	except Exception as e:
		print(e)
		return jsonify({"message":"Something went wrong while logging in"})