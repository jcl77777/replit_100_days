"""
🌟Star Wars Name Generator🌟

Input your first name > David

Input your lastname > Morgan

Input your mother's maiden name > Jones

Input the city where you were born > Cardiff

Your Star Wars name is Davmor Joiff
"""

contact = []

def printList():
  print()
  for item in contact:
    print(item)
  print()

#create Star Wars name based on four inputs
def generateName(first_name, last_name, mother_maiden_name, city):
  first = first_name[:2].capitalize()
  last = last_name[:2].lower()
  name = first + last
  
  maiden = mother_maiden_name[:2].capitalize()
  city = city[:2].lower()
  place = maiden + city
  return name + " " + place


while True:
  firstName = input("First name: ").strip().capitalize()
  lastName = input("Last name: ").strip().capitalize()
  mom = input("Mom's maiden name: ").strip().capitalize()
  city = input("Where were you born in? : ").strip().capitalize()

  swName = generateName(firstName, lastName, mom, city)
  
  if swName not in contact:
    contact.append(swName)
    print("added to the list successfully.")
    print(f"Welcome {swName} to Star Wars.")
    printList()
  elif swName in contact:
    print(f"{swName} already in the list.")
    printList()