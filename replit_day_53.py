'''
🌟RPG Inventory🌟

1: Add  2: Remove  3: View  > 1

Input the item to add: > Mana potion
Mana potion has been added to your inventory.

1: Add  2: Remove  3: View  > 2

Input the item to remove: > Sword
Sword has been removed from your inventory.

1: Add  2: Remove  3: View  > 3

Input the item to view: > Wizard's sleeve
You have 2 Wizard's sleeve
'''
inventory = []

print("🌟RPG Inventory🌟")

def add():
    item = input("Input the item to add: > ").capitalize()
    inventory.append(item)
    print(f"{item} has been added to your inventory.")

def remove():
    item = input("Input the item to remove: > ").capitalize()
    if item in inventory:
        inventory.remove(item)
        print(f"{item} has been removed from your inventory.")
    else:
        print(f"{item} is not in your inventory.")

def view():
    item = input("Input the item to view: > ").capitalize()
    count = inventory.count(item)
    if count > 0:
        print(f"You have {count} {item}")
    else:
        print(f"You do not have {item}")

def menu():
    action = input("1: Add  2: Remove  3: View  > ")
    if action == "1":
        add()
    elif action == "2":
        remove()
    elif action == "3":
        view()
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
        
#autoload
try:
  f = open("inventory.txt","r")
  inventory = eval(f.read())
except Exception as e1:
  print(f"ERROR: Unable to load {e1}")
  
while True:
  menu()
  #autosave
  try:
    f = open("inventory.txt", "w") 
    f.write(str(inventory)) 
    f.close()
  except Exception as e2:
    print(f"ERROR: Unable to load {e2}")