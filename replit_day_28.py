import random
import time
import os

# clear the window for the user to focus
def clear():
    os.system("clear")

# random dice number for health and strength stats
def dice(number):
    return random.randint(1, number)

# characters creation: choose among 4
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

# health stat
def health():
    return (dice(6) * dice(12)) / 2 + 10

# strength stat
def strength():
    return (dice(6) * dice(12)) / 2 + 12

# display info of the character
def display_character(name, chosen_race, health_stat, strength_stat):
    clear()
    print(f"Your character is {name} the {chosen_race} and has {health_stat} health and {strength_stat} strength")
    time.sleep(1)

# initiate the creation
def create_character():
    chosen_race = get_valid_race()
    return chosen_race, health(), strength()

def fight_loop(player1, player2):
  # Fight logic
  player1_attack_count = 0
  player2_attack_count = 0
  while True:
      player1_attack = dice(4)
      print(f"{user_name1} attacks with {player1_attack}")
      characters[1] = (characters[1][0], characters[1][1], max(0,characters[1][2] - player1_attack), characters[1][3])
      print("Player 1 health: ", characters[0][2], "Player 2 health: ", characters[1][2])
      player1_attack_count +=1

      if characters[1][2] <= 0:
          print(f"{characters[0][0]} wins with {player1_attack_count} hits!! {characters[1][0]} has been defeated.")
          break

      player2_attack = dice(4)
      print(f"{user_name2} attacks with {player2_attack}")
      characters[0] = (characters[0][0], characters[0][1], max(0,characters[0][2] - player2_attack), characters[0][3])
      print("Player 1 health: ", characters[0][2], "Player 2 health: ", characters[1][2])
      player2_attack_count +=1


      if characters[0][2] <= 0:
          print(f"{characters[1][0]} wins with {player2_attack_count} hits! {characters[0][0]} has been defeated.")
          break


# empty list of character selection
characters = []
print("Welcome to the Dungeon!")
print("Let's create your character(s)!")

# Player 1
user_name1 = input("What is your name Player1 ? ")
chosen_race, health_stat, strength_stat = create_character()
characters.append((user_name1, chosen_race, health_stat, strength_stat))
display_character(user_name1, chosen_race, health_stat, strength_stat)

# Player 2
user_name2 = input("What's your name Player2 ? ")
chosen_race, health_stat, strength_stat = create_character()
characters.append((user_name2, chosen_race, health_stat, strength_stat))
display_character(user_name2, chosen_race, health_stat, strength_stat)

clear()
print("Let's fight!")
time.sleep(1)
print("Fight!")
clear()

# Call the function
fight_loop(characters[0], characters[1])