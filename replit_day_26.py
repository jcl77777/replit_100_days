from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    stop = int(input("Press 2 to pause anytime. "))
    if stop == 2:
      source.paused = True
      return
    else:
      continue
      
while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  print(f"🎵 POD Music Player")
  time.sleep(2)
  user = int(input("Press 1 to Play, Press 3 to Exit "))
  # take user's input
  if user == 1:
    print("Play!")
    play()
  elif user == 3:
    print("Exiting and have a nice day...")
    exit()
  else:
    continue