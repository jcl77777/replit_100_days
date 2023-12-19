second = 1
minute = second * 60
hour = minute * 60
day = hour * 24

thisYear = int(input("What year is today? :"))
if thisYear % 4 == 0:
  year = day * 366 
  print("This is a Leap Year, we will have " + str(year) + " seconds")
else:
  year = day * 365 
  print("This is not a Leap Year, we will have " + str(year) + " seconds")

