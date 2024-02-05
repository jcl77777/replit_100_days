from flask import Flask, request

app = Flask(__name__)

# Dictionary to store user information
logins = {}

logins["miguel"] = {"username": "miguel", "password": "321"}
logins["cook"] = {"password": "123"}
logins["james"] = {"password": "456"}

@app.route("/login", methods=["POST"])
def login():
    form = request.form
    if form["username"] in logins:
        details = logins[form["username"]]
        if form["username"] == details["username"] and form["password"] == details["password"]:
            return f"You are logged in {form['username']}"
        else:
            return "Incorrect username or password."
    else:
        return "User does not exist."

@app.route('/')
def index():
    page = """
    <form action="/login" method="post">
    <p>Name: <input type="text" name="username" required> </p>
    <p>Password: <input type="password" name="password" required> </p>
    <button type="submit">Login</button>
    </form>
           """
    return page

app.run(host='0.0.0.0', port=81)