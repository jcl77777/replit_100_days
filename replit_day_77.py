from flask import Flask, redirect
import datetime

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
  myName = "JC"
  title = "JC's Portfolio"
  time = datetime.date.today()
  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{name}", myName) # Replace all instances of {name} with the contents of the 'myName' variable
  page = page.replace("{title}", title)
  page = page.replace("{time}", time) # Replace all instances of {title} with the contents of the 'title'
  return page

@app.route('/blog')
def blog():
  myName = "JC"
  page = ""
  f = open("template/blog.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{name}", myName)
  return page

app.run(host='0.0.0.0', port=81)
