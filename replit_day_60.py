'''
🌟Event Countdown Timer🌟

Input the event > Nan's 100th birthday

Input the year > 2022

Input the month > 10

Input the day > 16

🎉🎉Nan's 100th birthday is today! 🎉🎉
'''

import datetime

def countdown_timer():
  event_topic = input("Input the event > ")
  year = int(input("Input the year > "))
  month = int(input("Input the month > "))
  day = int(input("Input the day > "))

  #record userinput date
  event_date = datetime.date(year, month, day)
  today = datetime.date.today()
  #calculate the date delta btw event date and today
  delta = (event_date - today).days

  if delta > 0:
    print(f"{event_topic} is coming in {delta} days!")
  elif delta == 0:
    print(f"{event_topic} is today! Let's enjoy it!")
  elif delta < 0:
    print(f"Hope you enjoyed {event_topic}!")

print("🌟Event Countdown Timer🌟")
countdown_timer()