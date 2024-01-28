from flask import Flask

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
  page = f"""
  <html>
  <body>
  <p><a href = "/linktree">Go to Linktree</a></p>
  </body>
  </html>"""
  
  return page

@app.route('/portfolio') 
def portfolio():
  page = f"""<html>

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>My Portfolio</title>
    <link href="replit_day_74.css" rel="stylesheet" type="text/css" />
  </head>


  <body>
    <h1>JC's Portfolio</h1>
    <h2>Day 56 - 🌟Streamed Songs🌟 </h2>
      <p class="blurb">using your newly acquired csv reading and file management powers to work with data about a music streaming service.</p>
      <img src="image1.jpg" width = 30%>
      <p><a href = "https://github.com/jcl77777/replit_100_days/blob/main/replit_day_56.py">Link to github</a></p>
    <h2>Day 57 - 🌟Factorial Finder🌟</h2>
      <p>Recursion is a type of program where you get a subroutine to call itself.</p>
      <img src="image2.jpg" width = 30%>
      <p><a href = "https://github.com/jcl77777/replit_100_days/blob/main/replit_day_57.py">Link to github</a></p>

    <h2>Day 60 - 🌟Event Countdown Timer🌟</h2>
      <p class="blurb">Events countdown timer to automatically identify how far you are with the targeted day or already away...?</p>
      <img src="image3.jpg" width = 30%>
      <p><a href = "https://github.com/jcl77777/replit_100_days/blob/main/replit_day_60.py">Link to github</a></p>

    <h2>Day 65 - Object Oriented Programming </h2>
      <p>OOP Exacmple with Character Creation - Object Oriented Programming (OOP) is a programming paradigm that is based on classes and objects, which store all of their data and behaviors inside them. </p>
      <img src="image4.jpg" width = 30%>
      <p><a href = "https://github.com/jcl77777/replit_100_days/blob/main/replit_day_65.py">Link to github</a></p>

    <h2>Day 71 - 🌟Login System with Hashing🌟</h2>
      <p>Hashing is used to protect users' password by turning your password into a sequence of numbers, then passing it though a hashing algorithm</p>
      <img src="image5.jpg" width = 30%>
      <p><a href = "https://github.com/jcl77777/replit_100_days/blob/main/replit_day_71.py">Link to github</a></p>

<p><a href = "/">Go Home</a></p>

  </body>
</html>



  """

  return page

@app.route('/linktree')
def linktree():
  page = f"""
  <html>

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Linktree</title>
    <link href="replit_day_75.css" rel="stylesheet" type="text/css" />
  </head>

  <body>
    <h1>JC's Linktree</h1>

    <img src="linktree_profile.jpeg" width = 30%>
    <h2>About JC</h2>
      <p class="blurb">Learning among the space</p>

    <h2>Socials</h2>
    <ul>
      <li><a href = "https://www.linkedin.com/in/jung-chen-lee/">Link to Linkedin</a></li>
      <li><a href = "https://github.com/jcl77777/">Link to Github</a></li>
      <li><a href = "https://github.com/jcl77777/replit_100_days/">Link to My replit 100 Days</a></li>
    </ul>

<p><a href = "/portfolio">Go to portfolio</a></p>

  </body>
</html>"""

  return page



app.run(host='0.0.0.0', port=81)
