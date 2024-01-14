'''
🌟Palindrome Checker🌟

Input a word > Racecar

Racecar is a palindrome. Yay!
'''

print("🌟Palindrome Checker🌟")

def check():
    word = input("Input a word > ").lower()
    #[::-1] means start at the end of the string and end at position 0, move with the step -1, meaning one step backwards
    reverse_word = word[::-1]
    if word == reverse_word:
        print(f"{word} is a palindrome. Yay!")
    else:
        print(f"{word} is not a palindrome. Oh no!")

check()