from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def home():
	return render_template("login.html")

@app.route("/library")
def library():
	return render_template("library.html")

@app.route("/login", methods=["POST", "GET"])
def login():
	error = None
	if request.method == "POST":
		if request.form['username'] != 'username' or request.form['password'] != 'password':
			error = 'Incorrect password. Please try again.'
		else:
			return redirect(url_for("library"))
	return render_template('login.html', error=error)

masterlist = []

@app.route("/library", methods=["POST", "GET"])
def add():
	if request.method == "POST":
		book = Book(request.form['title'], request.form['author'], request.form['genre'])
	return render_template('library.html')

if __name__ == "__main__":
	app.run(debug=True)
