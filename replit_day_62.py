from replit import db
import datetime
import os
import time

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
  keys = list(db.keys())
  keys.sort(reverse=True)  # Sort keys in descending order (most recent first)
  # keys = keys[::-1]  # Reverse the list to display in descending order
  counter = 0
  for key in keys:
    print(f"{key}:\n{db[key]}\n")
    print()
    counter +=1
    opt = input("Next or exit? ").lower()

    if opt == "e":
      break
    #check if more stories to show
    elif counter >= len(keys):
      print("No more stories to show.")

def security():
  password = input("Password: ")
  if password == "123":
    return True
  else:
    print("Access Denied. Incorrect password")
    return False

while True:
  if security():
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