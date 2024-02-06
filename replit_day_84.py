from replit import db
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    # Check if username exists in the database
    if username in db:
        # Verify the password (here, you should compare hashed passwords)
        if db[username] == password:
            return f"Welcome back, {username}!"
        else:
            return "Invalid username or password"
    else:
        return "User does not exist"


@app.route("/create", methods=["POST"])
def create_user():
    username = request.form.get("username")
    password = request.form.get("password")

    # Check if the username already exists
    if username in db:
        return "Username already exists"
    else:
        db[username] = password
        return f"New user created successfully. Hello, {username}!"


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