import random

player_dict = {}

stat = ["intel", "speed", "power"]

def add_to_dict(name, intel, speed, power):
    player_dict[name] = {"intel": intel, "speed": speed, "power": power}

def battle(name1, name2):
    stat_choice = input(f"Choose your weapon for the battle between {name1} and {name2} (intel/speed/power)> ")

    if stat_choice in stat:
        stat1 = int(player_dict[name1][stat_choice])
        stat2 = int(player_dict[name2][stat_choice])

        if stat1 > stat2:
            print(f"{name1} wins! {name1} has a {stat_choice} stat of {stat1} and {name2} has a {stat2}")
        elif stat1 < stat2:
            print(f"{name2} wins! {name1} has a {stat_choice} stat of {stat1} and {name2} has a {stat2}")
        else:
            print(f"It's a tie! {name1} has a {stat_choice} stat of {stat1} and {name2} has a {stat2}")
    else:
        print("Invalid stat. Please choose between intel, speed, or power")

# Add players to the dictionary
add_to_dict("Cutecat", 120, 80, 90)
add_to_dict("Boldbat", 100, 95, 85)
add_to_dict("Swiftsnake", 99, 85, 120)
add_to_dict("Sneakymouse", 80, 120, 100)

while True:
    # Randomly pick two players
    name1, name2 = random.sample(player_dict.keys(), 2)
    print(f"{name1} vs {name2}")

    while True:
        battle(name1, name2)
        again = input("Do you want to play again? (yes/no)> ").lower()
        if again == "y":
            break
        elif again == "n":
            print("Happy Fighting!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")