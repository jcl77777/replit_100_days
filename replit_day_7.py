username = input("name: ")
dayOfTheWeek = input("day of the week: ")
favoriteNumber = input("favorite number: ")
favoriteDay = input("favorite day of the week: ")

if username == "dave" or "Dave":
  print("Hi Dave!")
elif username == "sally" or "Sally":
  print("Hey Sally!")


if dayOfTheWeek == favoriteDay:
    print("You have the same favorite day!")
else:
    print("You don't have the same favorite day.")

print("Hello, " + username + "." + "Today is " + dayOfTheWeek + "." + "Your favorite number is " + favoriteNumber + ".")