import random
import time
import os
import sys

#clear the window for user to focus
def clear():
    os.system("clear")

#random dice number for health and strength stats
def dice(number):
    return random.randint(1, number)

#characters creation: choose among 4 
def get_valid_race():
    # Create a dictionary to map abbreviations to full names
    race_mapping = {
        'W': 'Warriors',
        'M': 'Mages',
        'A': 'Archers',
        'T': 'Thieves'
    }
    while True:
        race = input("What is your race? (W)arriors, (M)ages, (A)rchers, (T)hieves? Enter W/M/A/T: ").upper()
        if race in race_mapping:
            return race_mapping[race]
        else:
            print("Invalid race. Please enter W, M, A, or T.")

#health stat
def health():
    return (dice(6) * dice(12)) / 2 + 10

#strength stat
def strength():
    return (dice(6) * dice(12)) / 2 + 12

#display info of the character
def display_character(name, chosen_race, health_stat, strength_stat):
    clear()
    print(f"Your character is {name} the {chosen_race} and has {health_stat} health and {strength_stat} strength")
    time.sleep(1)

#initiate the creation
def create_character():
    chosen_race = get_valid_race()
    return chosen_race, health(), strength()

#empty list of character selection
characters = []
print("Welcome to the Dungeon!")
print("Let's create your character(s)!")

while True:
    user_name = input("What is your name? ")
    while True:
        #multiple assignment
        chosen_race, health_stat, strength_stat = create_character()
        #show info
        display_character(user_name, chosen_race, health_stat, strength_stat)

        action = input("Do you like to regenerate, create another or exit? (R)egenerate, (C)reate another, (E)xit ")
        if action.lower() == "r":
            continue
        elif action.lower() == "c":
            characters.append((user_name, chosen_race, health_stat, strength_stat))  # Store the character's name and stats
            break
        elif action.lower() == "e":
            characters.append((user_name, chosen_race, health_stat, strength_stat))  # Store the character's name and stats
            clear()
            print("Thank you for playing with these characters! Have a great adventure!")
            for character in characters:
                print(f"{character[0]} - Race: {character[1]} - Health: {character[2]} - Strength: {character[3]}")
            sys.exit()
        else:
            print("Invalid option. Please enter 'R', 'G', or 'Q'.")
