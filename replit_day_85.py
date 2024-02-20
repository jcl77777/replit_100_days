from flask import Flask, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = os.environ['sessionKey']

@app.route('/')

def index():
  page = ""
  myName = ""
  if session.get("myName"):
    myName = session["myName"]
  page += f"""<h1>{myName}</h1> 
  <p>Login Out <input type='submit' value='Logout'></p>"""
  f = open("form.html", "r")
  page += f.read()
  f.close()
  return page

@app.route("/setName", methods=["POST"])

def setName():
  session["myName"] = request.form["name"]
  return redirect("/")

@app.route("/reset")
def reset():
  session.clear()
  return redirect("/")

app.run(host='0.0.0.0', port=81)