import random
import os
import time

def createCard():
  values = []
  for i in range(8):
    number = random.randint(0, 90)
    # numbers not repeated
    if number in values:
        continue
    # numbers added to the list
    else:
        values.append(number)

  # numbers sorted
  values.sort()

  # Create a bingo list with three sublists
  bingo_list = [
    [values[0], values[1], values[2]],
    [values[3], "BINGO", values[4]],
    [values[5], values[6], values[7]]
  ]
  return bingo_list

bingo_card = createCard()

while True: 
  # Print each row
  for row in bingo_card:
    print(row)
  guess = int(input("guess a number btw 1 and 90: "))
  for row in range(3):
    for item in range(3):
      if bingo_card[row][item] == guess:
         bingo_card[row][item] = "x"
      
  counter = 0
  for row in bingo_card:
    for item in row:
      if item == "x":
        counter += 1
  if counter == 8:
    print("You won the game!")
    break
  
#need to review different solutions