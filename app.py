from flask import Flask, render_template, json, request

app = Flask(__name__)

@app.route("/")
def main():
  return render_template('home.html')

@app.route("/showSignUp")
def showSignUp():
	return render_template('signup.html')

@app.route("/signUp", methods=['POST'])
def signUp():
	_name = request.form['inputName']
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']

	if _name and _email and _password:
		return json.dumps({'html':'<span>Thanks for signing up!</span>'})
	else:
		return json.dumps({'html':'<span>Please fill in all the fields</span>'})

if __name__ == "__main__":
  app.run()
