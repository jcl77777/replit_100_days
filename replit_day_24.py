import random

def dice():
  while True:
    try:
      number = int(input("Pick a number to roll a dice. > "))
      diceNumber = random.randint(1, number)
      print("You rolled", diceNumber)
      
      rollStart = input("Roll again? (y/n) ").lower()
      
      if rollStart == "y":
        continue
      else:
        print("See you next time!")
        break
    except ValueError:
      print("Please enter a valid number.")

dice()

# shorter version
# import random
# print("Infinity Dice 🎲")
  
# sides = int(input("How many sides?: "))
# playGame = "yes"
  
# def rollDice(sides):
#   print("You rolled ", random.randint(1,sides))
# while playGame == "yes":
#     rollDice(sides)
#     playGame = input("Roll again?")