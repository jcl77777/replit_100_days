import random

print("Welcome to number guessing game!")
print("Guess a number between 1 and 1000.")
print("During the game, I will let you know if your guess is too high or too low.")
print("Let's start!")
print("")

number = random.randint(1, 1000)
counter = 0

while True:
  try:
    pickANumber = int(input("Pick a number btw 1 and 1000: "))

    #handle negative numbers
    if pickANumber < 0:
      print("Not counted! This is a negative number")
      continue

    #handle number comparisons >=<
    if pickANumber < number:
      print("Too low")
      counter +=1
      print("Tried", counter, "times")
    elif pickANumber > number:
      print("Too high")
      counter +=1
      print("Tried", counter, "times")
    elif pickANumber == number:
      print("Bingo!")
      counter +=1
      print("Succeeded in", counter, "times")
      break
    else:
      continue

  #handle non-number entry
  except ValueError:
    print("That's not a number!")