import random

print("Welcome to Random One-Million-to-One")
print("Pick a number between 1 and 1000000")
print("Are you ready? ")

while True:
    myNumber = random.randint(1, 10)
    countGuess = 0

    while True:
      try:
          playerGuess = int(input("Guess a number: "))

          if playerGuess == myNumber:
              print("You guessed it!")
              countGuess += 1
              break
          elif playerGuess < 1 or playerGuess > 1000000:
              print("Please guess a number between 1 and 1000000.")
          elif playerGuess > myNumber:
              print("Too high")
              countGuess += 1
          elif playerGuess < myNumber:
              print("Too low")
              countGuess += 1
          else:
              print("Invalid guess")

      except ValueError:
          print("Please enter a valid number.")

    print(f"It took you {countGuess} guesses to get the correct number!")

    playerStart = input("Click run to play again! (Enter 'run') ")

    if playerStart.lower() != "run":
      print("Hope you had fun!")
      break