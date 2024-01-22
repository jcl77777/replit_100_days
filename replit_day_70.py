'''
🌟Login System🌟

Username > admin01

Password > thepowerTHEPOWER

Hello admin
'''

import os

#store the key value pair adminusername = admin01 & adminpassword = adminpass
username = os.environ['adminusername']
password = os.environ['adminpassword'] # Uses the os library to talk to the environment and get the secret password stored there.

print("🌟Login System🌟")

while True:
  userName = input("Username > ")
  userPass = input("Password > ")
  #check the user and the password altogether
  if userName == username and userPass == password:
    print("Hello Admin")
    break
  else:
    print("Try again. ")