from app import app

@app.route("/canteen")
def canteen():
	return "Welcome to canteen page"