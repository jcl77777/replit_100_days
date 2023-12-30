'''
🌟Website Rating🌟

Input the website name: Replit

Input the URL: replit.com

Input your a description: An awesome online IDE.

Input the a star rating out of 5: *****

name:Replit, URL:replit.com, description:An awesome online IDE, rating:*****
'''

db = {}
print("🌟Website Rating🌟")

websiteName = input("Input the website name: ")
url = input("Input the URL: ")
description = input("Input your description: ")

while True:
  try:
      rating = int(input("Give a rating between 1 - 5 stars: "))
      if 1 <= rating <= 5:
          db["websiteName"] = websiteName
          db["url"] = url
          db["description"] = description
          db["rating"] = rating
          break
      else:
          print("Please provide a rating between 1 and 5 only.")
          continue
  except ValueError:
      print("Please enter a valid numeric rating.")
      continue
    
#show all info after successfully inserting
print("Stored successfully.")
for i in db:
  print(db[i])

print(f"Your {websiteName} with {url} is stored in the database. It serves {description} and has a rating of {rating} stars.")