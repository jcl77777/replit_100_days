contact =[]

def printList():
  print()
  for item in contact:
    print(item)
  print()
  
while True:
  firstName = input("First name: ")
  lastName = input("Last name: ")
  name = firstName.strip().capitalize() + " " + lastName.strip().capitalize()
  if name not in contact:
    contact.append(name)
    print(f"{name} added to the list.")
    printList()
  elif name in contact:
    print(f"{name} already in the list.")
    printList()
  else: 
    print("Please enter a valid input.")