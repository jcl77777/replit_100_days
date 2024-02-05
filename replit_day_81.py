from flask import Flask, request

app = Flask(__name__)

@app.route("/robot", methods =["Post"])
def robot():
  form = request.form
  if form["metal"] == "yes":
    return "You are a metal robot."
  elif form["food"] == "Oil":
    return "You are definitely a robot."
  elif form["infinity"] != 2:
    return "What are you exactly...? Robot."
  else:
    return "Hello fellow human friend."

@app.route('/')
def index():
    page = ""
    f = open("robot.html", "r")
    page = f.read()
    f.close()
    return page

app.run(host='0.0.0.0', port=81)
