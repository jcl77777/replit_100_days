"""
To Do List Manager:
Do you want to view, add, or edit your to do list?
view

Record video for day 34
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
    toDoList.append(item)
    print(f"{item} added successfully. ")
    clear()
  elif menu == "remove":
    item = input("What should I remove from the To Do list?: ")
    if item in toDoList:
      toDoList.remove(item)
      print(f"{item} removed successfully. ")
      clear()
    else:
      print(f"{item} was not in the list")
      clear()
  elif menu == "edit":
    old_item = input("Which item should I edit?: ")
    new_item = input("What should I replace it with?: ")
    if old_item in toDoList:
        index = toDoList.index(old_item)
        toDoList[index] = new_item
        print(f"{item} replaced successfully. ")
        clear()
    else:
      print(f"{old_item} was not in the list")
      clear()
  elif menu == "view":
    printList()
    clear()
  else:
    print("That is not a valid option. Try again!")
    clear()