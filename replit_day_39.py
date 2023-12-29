'''
🌟Hangman🌟

Choose a letter: i
Nope, not in there.
5 left.

Choose a letter: a
Correct!
__a__

Choose a letter: s
Correct!
s_a__

Choose a letter: u
Correct!
sua__

# Repeat until.....
# If user wins
You won with 5 lives left.

# Loses
You lost!
'''
import random

def display_word(word, guessed_letters):
  displayed_word = ""
  for i in word:
      if i in guessed_letters:
          displayed_word += i
      else:
          displayed_word += "_"
  return displayed_word

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]
word = random.choice(listOfWords)
number = len(word)
lives = number
guessed_letters = []
print("Welcome to 🌟Hangman🌟")
print(f"Got {lives} times to avoid being hang!")

while lives > 0:
  letter = input(f"Choose a letter: ").lower()
  if letter in guessed_letters:
     print("Tried that already!")
     continue
  
  if letter in word:
    guessed_letters.append(letter)
    print("Correct!")
  else:
    print("Incorrect!")
    lives -=1
    print(f"{lives} lives left.")
    
  displayed_word = display_word(word, guessed_letters)
  print(displayed_word)

  if "_" not in displayed_word:
      print("Congratulations! You guessed the word!")
      break
if lives == 0:
  print("Game Over! You are a dead man now!")
