from flask import Flask

#store the data
myReflections ={}

#random entry to test
myReflections["77"] = {"link": "https://github.com/jcl77777/replit_100_days/blob/main/replit_day_77.py", "reflection": "Like it."}
myReflections["78"] = {"link": "https://github.com/jcl77777/replit_100_days/blob/main/replit_day_78.py", "reflection": "Make it to Day 78."}

app = Flask(__name__)

@app.route('/<pageNumber>')
def index(pageNumber):
    page = ""
    f = open("template/reflection.html", "r")
    page = f.read()
    link = myReflections[pageNumber]["link"]
    reflection = myReflections[pageNumber]["reflection"]
    page = page.replace("{day}", pageNumber) 
    page = page.replace("{link}", link)
    page = page.replace("{reflection}", reflection) 
    return page

app.run(host='0.0.0.0', port=81)