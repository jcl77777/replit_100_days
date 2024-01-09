#autoload and autosave external file 

import time
import os

toDoList = []
priorityList = [
    "High",
    "Medium",
    "Low"
]

#autoload
f=open("calendar.txt","r") # Only need read permissions here
toDoList = eval(f.read())
f.close()
########################################

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
    for row in toDoList:
      if task in row:
        toDoList.remove(row)
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

  #autosave
  f = open("calendar.txt", "w") # Permissions set to 'w' because we are deleting the file and replacing it with the whole 2D list every time.
  f.write(str(toDoList)) # Need to cast the list to a single string
  f.close()