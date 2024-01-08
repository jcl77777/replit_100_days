'''
🌟Idea Storage🌟

Add an idea or see a random idea? a/r. > r

Monkey tennis.

Add an idea or see a ranmdom idea? a/r. > a

Input your idea. > Youth hostelling with Chris Eubank

Nice! Your idea has been stored.
'''

import random
import time
import os

file_path = "my_ideas.txt"
f = open(file_path, "a+")

print("🌟Idea Storage🌟")

def add_idea():
  add = input("Input your idea to add. > ")
  f = open(file_path, "a")
  #write a line to next line
  f.write(add + "\n")
  print("idea added successfully")
  return add

def remove_idea():
  remove = input("Input existing idea to remove. > ")
  #read the file to split to lines
  f = open(file_path, "r")
  lines = f.readlines()
  #define which line to overwrite
  f = open(file_path, "w")
  for line in lines:
    if line.strip() != remove:
      f.write(line)
  print("idea removed successfully")
  return remove

def menu():
  choice = input("Add or remove an idea, see a random idea or quit the menu? a/r/l/q. > ")
  return choice

def load_random():
  #read the file
  f = open(file_path, "r")
  contents = f.read()
  #split to lines
  contents = contents.split()
  if contents:
    print(random.choice(contents))
  else:
    print("No ideas available.")

while True:
  choice = menu()
  if choice == "a":
    add = add_idea()
    time.sleep(1)
    os.system("clear")
  elif choice == "r":
    remove = remove_idea()
    time.sleep(1)
    os.system("clear")
  elif choice == "l":
    load_random()
  elif choice == "q":
    print("Have a nice day!")
    break
  else:
    print("Invalid input. Please input a, r, l or q.")