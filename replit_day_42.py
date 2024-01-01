'''
👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾

Input your beast's name > Brian

Input your beast's type > Earth

Input your beast's special move > Flying bellyflop

Input your beast's staring HP > 50

Input your beast's staring MP > 20

# This text outputs in green
Your beast is called Brian. It is an earth beast with a special move of Flying bellyflop
'''
import random

beastList = []

print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print("")

#color change to text 
def changeColor(text, color):
  if color == "red":
    print("\033[1;31m", text)
  elif color == "green":
    print("\033[1;32m", text)
  elif color == "yellow":
    print("\033[1;33m", text)
  elif color == "blue":
    print("\033[1;34m", text)
  elif color == "purple":
    print("\033[1;35m", text)
  elif color == "white":
    print("\033[1;37m", text)
  elif color =="default":
    print("\033[0m", text)
    
#random HP&MP
def HP():
  HP = random.randint(1,100)
  return HP
def MP():
  MP = random.randint(1,100)
  return MP

#color change based on type
def type(beastType):
  if beastType == "Earth":
    changeColor("Earth","yellow")
  elif beastType == "Fire":
    changeColor("Fire","red")
  elif beastType == "Water":
    changeColor("Water","blue")
  elif beastType == "Air":
    changeColor("Air", "white")
  elif beastType == "Spirit":
    changeColor("Spirit","purple")
  elif beastType == "Grass":
    changeColor("Grass","green")
  else:
    print("not a valid beast type. Try again!")

while True:
  beastName = input("Input your beast's name > ").strip().capitalize()
  #make sure the type is entered within the list
  while True:
    try:
      Type = ["Earth", "Fire", "Water", "Air", "Spirit", "Grass"]
      beastType = input("Input your beast's type (Earth/Fire/Air/Water/Spirit/Grass)> ").strip().capitalize()
      if beastType in Type:
        break
      else:
        print("Please enter a valid beast type. Try Again!")
        continue
    except:
      print("Please enter a valid beast type. Try Again!")
      continue
  beastMove = input("Input your beast's special move > ").strip()
  beastHP = HP()
  beastMP = MP()
  current_beast = {
    "Beast Name": beastName, 
    "Beast Type": beastType, 
    "Beast Move": beastMove, 
    "Beast HP": beastHP, 
    "Beast MP": beastMP
  }
  #store into the list
  beastList.append(current_beast)

  print(f"Your {beastName} is", end="")
  type(beastType)
  print(f"Its best attack is {beastMove}. It has {beastHP} HP and {beastMP} MP.")
  changeColor("","default")

  #break out the loop
  play_again = input("Do you want to input another beast? (yes/no) ").strip().lower()
  if play_again != "yes":
    print("Thanks for playing!")
    #print all entered beasts
    for beast in beastList:      
      print(beast)
    break