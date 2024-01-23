'''
🌟Login System🌟
1: Add User, 2: Login >  1
Username: > Kenny
Password: > L0gg1ns
Details stored.
1: Add User, 2: Login >  2
Username: > Kenny
Password: > L0gg1ns
Login successful
'''

from replit import db
import random

print("🌟Login System🌟")

#add new user and its password
def user_add():
  username = input("Username: > ")
  password = input("Password: > ")
  keys = db.keys()
  #check if username already exists
  if username in keys:
    print("ERROR: Username exists")
    return
  #randomly assign salt
  salt = random.randint(1000,9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  #store the key value pair
  db[username] = {"password": newPassword, "salt": salt}

  print("User added.")

#allow user to login
def login():
  username = input("Username: > ")
  password = input("Password: > ")
  keys = db.keys()
  #check if the username exists
  if username not in keys:
    print("ERROR: Username exists")
    return

  #check the info in the db associated with the username
  salt = db[username]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  
  if db[username]["password"] == newPassword:
    print("Login successfully.")
  else:
    print("Try again!")

  
while True:
  menu = input("1: Add User, 2: Login > ")
  if menu == "1":
    user_add()
  elif menu =="2":
    login()
  #show if the password is hashed
  else:
    keys = db.keys()
    for key in keys:
      print(db[key])