from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello! This is the main page <h1>HELLO<h1>"

@app.route("/<name>")
def user(name):
	return f"Hello {name}!"

@app.rout("/admin")
def admin():
	return redirect(url_for("home"))

if __name__ == "__main__":
	app.run()