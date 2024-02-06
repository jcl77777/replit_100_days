from replit import db
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/login', methods=["POST"])
def login():
    keys = db.keys()
    form = request.form
    # Check if username exists in the database
    if form["username"] in keys:
        # Verify the password (here, you should compare hashed passwords)
        if db[form["username"]] == form["password"]:
            return f"""Welcome back, {form["username"]}!"""
        else:
            return "Invalid username or password"
    else:
        return redirect ("/create")


@app.route("/create", methods=["POST"])
def create_user():
    keys = db.keys()
    form = request.form
    # Check if the username already exists
    if form["username"] in keys:
        #if exist, redirect to login page
        return redirect("/login")
    else:
        # Create a new user
        db[form["username"]] ={"password": form["password"]}
        return f"""New user created successfully. Hello, {db[form]["username"]}!"""


@app.route('/')
def index():
    page = """
    <form action="/login" method="post">
    <h3>Existing User</h3>
    <p>Name: <input type="text" name="username" required> </p>
    <p>Password: <input type="password" name="password" required> </p>
    <button type="submit">Login</button>
    </form>
    <form action="/create" method="post">
    <h3>New User</h3>
    <p>New User Name: <input type="text" name="username" required> </p>
    <p>New Password: <input type="password" name="password" required> </p>
    <button type="submit">Create User</button>
    </form>
    """
    return page


app.run(host='0.0.0.0', port=81)