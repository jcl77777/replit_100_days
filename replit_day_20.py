print("Welcome to number list generator.")
print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")
print()

while True:
  try:
    startNumber = int(input("Enter a starting number: "))
    if startNumber < 0:
      print("negative number unnacceptable. Please try again!")
      continue
      
    endNumber = int(input("Enter an ending number: "))
    if endNumber < 0:
      print("negative number unnacceptable. Please try again!")
      continue
    elif startNumber == endNumber:
      print("Same number entered. Please try again!")
      continue
      
    #increment input
    increment = int(input("How many you want to add/substract each time? "))

    #loops to print numbers
    for i in range (startNumber, endNumber, increment):
      print(i)
    break
    
  except ValueError:
    print("numbers only. Please try again!")
