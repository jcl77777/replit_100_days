mokedex = {}

def prettyPrint():
  print()
  for key, value in mokedex.items():
    print(key, end=": ")
    for subKey, subValue in value.items():
      print(subKey, subValue, end=" | ")
  print("\033[0m")

print("MokéBeast")
print()

while True: 
  name = input("Name: ").strip().title()
  type = input("Type: ").strip().title()
  specialMove = input("Special Move: ").strip().title()
  HP = input("HP: ").strip().title()
  MP = input("MP: ").strip().title()
  
  mokedex[name] = {"Type": type, "SpecialMove": specialMove, "HP": HP, "MP": MP}
  
  if mokedex[name]["Type"]=="Earth":
    print("\033[33m", end="")
  elif mokedex[name]["Type"]=="Air":
    print("\033[37m", end="")
  elif mokedex[name]["Type"]=="Fire":
    print("\033[31m", end="")
  elif mokedex[name]["Type"]=="Water":
    print("\033[34m", end="")
  else:
    print("\033[0m", end="")

  prettyPrint()