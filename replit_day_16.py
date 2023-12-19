print("Let's have a lyrics challenge!")
print("You will fill in the blank lyrics!")
print("see if you are as cool as me...?")
print("")

counter = 1
while True:
  fill = input("Never going to ______ you up. >")
  if fill.lower() == "put" or fill.lower() == "let" or fill.lower() == "give":
    break
  else:
    print("Try again")
    counter +=1
print("Well done! It only took you ", counter, "attempt(s).")