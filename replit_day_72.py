from replit import db
import datetime
import os
import time
import random

def clear():
  time.sleep(1)
  os.system("clear")

def add():
  add_story = input("What would you like to add to the story? ")
  timestamp = datetime.datetime.now()
  timestamp = str(timestamp)
  db[timestamp] = add_story
  print("Story added successfully!")

def view():
  #skip the username and password in the db
  keys = db.prefix("2")
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}{db[key]}""")
    print()
    opt = input("Next or exit? > ").lower()
    if opt == "e":
        break

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
    return True
  else:
    print("Access Denied. Incorrect password. Try again!")
    return False

keys = db.keys()
#create the account for the first time
if len(keys)<1:
    user_add()
else:
  while True:
    login()
    clear()
    menu = input("1: Add\n2: View\n")
    if menu == "1":
        add()
        clear()
    elif menu == "2":
        view()
        clear()
    else:
        print("Enter valid input. 1 or 2.")
        clear()
        break