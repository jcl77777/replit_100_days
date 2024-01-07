import os
import time

file_path = "high_score.txt"

f = open(file_path, "a+")

while True:
    initials = input("What's your three-letter initials? > ").strip()
    score = int(input("Provide your lucky number out of 100000 > "))

    f.write(f"{initials}, {score}\n")

    print(f"Hello {initials}, your lucky number {score} is added to the table.")

    again = input("Add another? (y/n) > ").strip().lower()
    time.sleep(1)
    os.system("clear")

    if again == "y":
        continue
    #show the file info
    elif again == "n":
        f.close()
        f = open(file_path, "r")
        print(f.read())
    else:
        print("Invalid input")
        break
    break

f.close()
