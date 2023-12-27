"""
To Do List Manager:

Do you want to view, add, edit, or remove an item from the to do list?
view

record the video for day 36

Do you want to view, add, edit, or remove an item from the to do list?
remove

What do you want to remove?
record the video for day 36

Are you sure you want to remove this?
yes
"""

import os
import time

toDoList = []

def printList():
  print() 
  for item in toDoList:
    print(item)
  print() 

def clear():
  time.sleep(2)
  os.system('clear')

while True:
  menu = input("Your Agile To Do List: add, edit, view or remove? ")
  if menu == "add":
    item = input("What should I add to the To Do list?: ")
    if item not in toDoList:
      toDoList.append(item)
      print(f"{item} added successfully. ")
      clear()
    elif item in toDoList:
      print(f"{item} already exists in the To Do list. ")
      clear()
  elif menu == "remove":
    item = input("What should I remove from the To Do list?: ")
    if item in toDoList:
      confirmation = input("Are you sure you want to remove this? y/n: ")
      if confirmation.lower() == "y":
        toDoList.remove(item)
        print(f"{item} removed successfully. ")
        clear()
      elif confirmation.lower() == "n":
        print("You chose not to remove this item.")
        clear()
      else:
        print("Please provide a valid response.")
        clear()
    else:
      print(f"{item} was not in the list")
      clear()
  elif menu == "edit":
    old_item = input("Which item should I edit?: ")
    new_item = input("What should I replace it with?: ")
    reconfirm = input("Are you sure you want to replace this? y/n: ")
    if old_item not in toDoList:
      print(f"{old_item} was not in the list")
      clear()
    elif old_item in toDoList and reconfirm.lower() == "y":
        index = toDoList.index(old_item)
        toDoList[index] = new_item
        print(f"{item} replaced successfully. ")
        clear()
    elif old_item in toDoList and reconfirm.lower() == "n":
      print("You chose not to edit this item.")
      clear()
    else:
      print("Please provide a valid response.")
  elif menu == "view":
    printList()
    clear()
  else:
    print("That is not a valid option. Try again!")
    clear()