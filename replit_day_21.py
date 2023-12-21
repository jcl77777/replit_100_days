print("You can inquire a multiplication table for the number you pick.")
print("The table will be generated automatically to show to the multiplication from 1 to 10.")
print("You will answer the questions to solve the table.")
print("Let's pick one number. ")
print("")

i = 0
playerScore = 0

try:
  number = int(input("What's your number? "))
  for i in range(1, 11):
    playerNumber = int(input("The table for the number " + str(number) + " is: " + str(number) + " x " + str(i) + " = " ))
    if playerNumber == number * i:
      playerScore +=1
      print("Correct!")
    elif playerNumber != number * i:
      print("Wrong! It should have been ", number * i)
      continue
except ValueError:
  print("Please, insert a number.")
  
if playerScore == 10:
  print("Congratulations! You got 10 questions right.")
else: 
  print("Your score:", playerScore, "out of ", i)

