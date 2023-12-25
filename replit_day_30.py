"""
30 Days Down

Day 1: 
Amazing

            You thought Day 1 was amazing.
Day 2:
so good that I bought the David plushie

              You thought Day 2 was so good...
"""
def dayPrint():
  for i in range(1, 31):
      daily = input(f"What did you feel about Day {i}? ")
      #store the value
      userInputs.append((i, daily))
      #print the result immediately
      print(f"Day {i}: {daily}")

      #authorize to continue the entry or exit
      while True:
          userExit = input("Would you like to exit? (y/n) ")
          if userExit.lower() == "y":
              display()
              print("Thank you for using the Daily Feelings")
              return
          elif userExit.lower() == "n":
              break  # Continue to the next day
          else:
              print("Please enter a valid response (y/n). Try again!")

#print all days' dairy
def display():
  for userInput in userInputs:
    print(f"Day: {userInput[0]} - Daily Feeling: {userInput[1]}")

userInputs = []
print("30 Days Down")
dayPrint()