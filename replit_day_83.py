from flask import Flask, request
import datetime

app = Flask(__name__, static_url_path="/static")

@app.route('/', methods = ["GET"])
def index():
  data = request.args
  background = "default"
  if data != {}:
    background = data["background"]
  myName = "JC"
  title = "JC's Portfolio"
  time = str(datetime.date.today())
  page = ""
  f = open("template/portfolio_day_83.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{name}", myName) 
  page = page.replace("{title}", title)
  page = page.replace("{time}", time) 
  page = page.replace("{background}", background)
  return page

app.run(host='0.0.0.0', port=81)