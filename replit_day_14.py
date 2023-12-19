from getpass import getpass as input

print("Let's play 🪨📄✂️")
print("Type S for Scissors, R for Rock, P for Paper")
print("Ready for your choice? ")
print("Let's begin!")

playerOne = str(input("Player 1, choose your weapon! "))
playerTwo = str(input("Player 2, choose your weapon! "))

# Check if playerOne entered a valid choice
if playerOne not in ["S", "R", "P"]:
    print("Player 1, type the right weapon!")

# Check if playerTwo entered a valid choice
elif playerTwo not in ["S", "R", "P"]:
    print("Player 2, type the right weapon!")

else:
    # Define winning combinations
    result = {
        "S": "P",  # Scissors beats Paper
        "R": "S",  # Rock beats Scissors
        "P": "R"   # Paper beats Rock
    }

    # Determine the winner
    if playerTwo == result[playerOne]:
        print("Player 1 wins!")
    elif playerOne == result[playerTwo]:
        print("Player 2 wins!")
    else:
        print("Tie!")
