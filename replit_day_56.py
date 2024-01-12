import csv
import os

print("🌟Streamed Songs🌟")

with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)

  #read each row in csv
  for row in reader:
    #translate each artist
    artist = row["Artist(s)"].title()
    #check if artist folder already exists
    if not os.path.exists(artist):
      os.mkdir(artist)
    #break down to each song
    song = row["Song"]
    #add song to artist folder
    path = os.path.join(f"{artist}/", song)
    f = open(path, "w")
    f.close()