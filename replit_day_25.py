import random
import sys

def dice(sides):
    while True:
        try:
            diceNumber = random.randint(1, sides)
            return diceNumber
        except ValueError:
            print("Please enter a valid number.")

def health():
    healthNum1 = dice(6)
    healthNum2 = dice(8)
    healthNumber = healthNum1 * healthNum2
    return healthNumber

print("Welcome to the Dungeon of Doom!")
print("Warrior generator")
print("")

characters =[]

for i in range(3):
    name = input("What's the name of your warrior? > ")
    print(f"Let's see how potential {name} you are!")
    while True:
        healthNumber = str(health())
        print(f"The health metric of {name} is {healthNumber}")
        
        action = input("Do you want to (R)egenerate health, (G)enerate a new character, or (Q)uit? (r/g/q) ").lower()

        if action == 'r':
            continue  # Regenerate health for the same character
        elif action == 'g':
            characters.append((name, healthNumber))  # Store the character's name and health
            break  # Generate a new character
        elif action == 'q':
            characters.append((name, healthNumber))  # Store the character's name and health before quitting
            print("Thank you for playing with these characters! Have a great adventure!")
            for character in characters:
                print(f"{character[0]} - Health: {character[1]}")
            sys.exit()
        else:
            print("Invalid option. Please enter 'R', 'G', or 'Q'.")
    if i == 2: 
        print("You have generated the maximum of three characters.")
        for character in characters:
                print(f"{character[0]} - Health: {character[1]}")