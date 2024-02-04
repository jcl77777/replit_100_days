from flask import Flask, request

app = Flask(__name__)

# Dictionary to store user information
logins = {}

logins["miguel"] = {"password": "321"}
logins["cook"] = {"password": "123"}
logins["james"] = {"password": "456"}

@app.route("/login", methods=["POST"])
def login():
    form = request.form
    isThere = False
    details ={}
    try:
      details = logins[form["username"]]
      isThere = True
    except:
      return "Incorrect username or password."

    if form["password"] == details["password"]:
      return "You are logged in."
    else:
      return "Incorrect username or password."


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