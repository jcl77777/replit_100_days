from getpass import getpass as input

print("Let's play 🪨📄✂️")
print("Type S for Scissors, R for Rock, P for Paper")
print("Ready for your choice? ")
print("Let's begin!")
print("")

counter1 = 0
counter2 = 0

while True:
    playerOne = str(input("Player 1, choose your weapon! "))
    playerTwo = str(input("Player 2, choose your weapon! "))

    # Check if players enter a valid choice
    if playerOne not in ["S", "R", "P"] or playerTwo not in ["S", "R", "P"]:
        print("Invalid Weapon. Please try Again.")
        continue
    # Define winning combinations
    result = {
        "S": "P",  # Scissors beats Paper
        "R": "S",  # Rock beats Scissors
        "P": "R"  # Paper beats Rock
    }

    # Determine the winner
    if playerTwo == result[playerOne]:
        print("Player 1 wins!")
        counter1 += 1
        print("Player One: {} Player Two: {}".format(counter1, counter2))
    elif playerOne == result[playerTwo]:
        print("Player 2 wins!")
        counter2 += 1
        print("Player One: {} Player Two: {}".format(counter1, counter2))
    else:
        print("Tie!")

  # Check if players have won 3 times
    if counter1 == 3:
        print("Player One WON the game!")
        break
    elif counter2 == 3:
        print("Player Two WON the game!")
        break
    else:
      continue

print("Thank you for having this awesome game!")