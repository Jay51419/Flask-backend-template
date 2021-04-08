from app import app

@app.route("/login",methods=['POST'])
def login():
	return "Welcome to lgin page"