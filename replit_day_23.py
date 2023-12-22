def login():
  while True:
      username = input("What's your name? ")
      password = input("What's your password? ")

      if username == "david" and password == "baldies4life":
          print("Welcome to Replit!")
          break
      else:
          print("Whoops! I don't recognize that username or password. Try again!")

print("Replit Login System")
# Call the login function
login()