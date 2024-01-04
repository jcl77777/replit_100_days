'''
🌟Life Organizer🌟

Welcome to the life organizer. Do you want to add, view, edit or remove a to do? > Add

What is the task? > Pay teachers more.
When is it due by? > 11/01/2022
What is the priority? >  High

Thanks, this task has been added.

Do you want to see the menu again or quit? > quit.
'''
import time
import os

toDoList = []
priorityList = [
    "High",
    "Medium",
    "Low"
]
def prettyPrint():
  print()
  for item in toDoList:
    print(item)
  print()

def clear():
  time.sleep(2)
  os.system('clear')

print("🌟Life Organizer🌟")

while True:
  
  action = input("Welcome to the life organizer. Do you want to add, view, edit, remove a to do or quit? (a/v/e/r/q)> ").strip().lower()
  #add
  if action == "a":
    task = input("What is the task?> ")
    due = input("When is it due by? (DD/MM/YYYY)> ")
    while True:
      priority = input("What is the priority? (Low/Medium/High) > ").strip().capitalize()
      if priority not in priorityList:
        print("Please provide a valid priority (Low/Medium/High).")
      else:
        new_task = f"Task: {task}, Due: {due}, Priority: {priority}"
        toDoList.append(new_task)
        print("Thanks, this task has been added successfully.")
        prettyPrint()
        clear()
        break
  #view
  elif action == "v":
    if len(toDoList) == 0:
      print("No tasks found.")
    else:
      prettyPrint()
      clear()

  #edit
  elif action == "e":
    prettyPrint()
    task = input("Which task would you like to edit? > ").strip()
    for i in range(len(toDoList)):
      if task in toDoList[i]:
        update_task = input("What is the new task? > ").strip()
        update_due = input("When is it due by? (DD/MM/YYYY) > ").strip()
        while True:
           update_priority = input("What is the new priority? (Low/Medium/High) > ").strip().capitalize()
           if update_priority in priorityList:
              break
           else:
              print("Please provide a valid priority (Low/Medium/High).")
              continue
        toDoList[i] = f"Task: {update_task}, Due: {update_due}, Priority: {update_priority}"
        print("Task updated successfully.")
        prettyPrint()
        clear()
        break
      else:
        print("Task not found.")

  
  #remove
  elif action == "r":
    prettyPrint()
    task = input("Which task you would like to remove? > ")
    #check each item in the list
    if task in toDoList:
      toDoList.remove(task)
      print("task removed successfully.")
      prettyPrint()
      clear()
    else:
      print("Task not found.")
      clear()
  #quit
  elif action == "q":
    print("Thanks for using the life organizer. Goodbye!")
    break
  
  #invalid input
  else:
    print("Invalid action. Please choose a/v/e/r/q.")
    clear()


'''
# | Name | Date | Priority
import os, time
todo = []

def add():
  time.sleep(1)
  os.system("clear")
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in todo:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  time.sleep(1)

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to edit > ")
  found = False
  for row in todo:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in todo:
    if find in row:
      todo.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to remove > ")
  for row in todo:
    if find in row:
      todo.remove(row)

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()

  time.sleep(1)
  os.system("clear")
'''