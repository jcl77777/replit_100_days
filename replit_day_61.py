from replit import db
import datetime
import os
import time

def clear():
  time.sleep(1)
  os.system("clear")

def add():
    tweet = input("Tweet > ")
    #store the created time
    timestamp = datetime.datetime.now()
    key = f"{timestamp}"
    #store key value pair - timestamp: tweet
    db[key] = tweet
    print("Tweet posted successfully.")

def view():
    # Convert keys to a list to avoid modification during iteration
    keys = list(db.keys())  

    if not keys:
        print("No tweets available.")
        return

    tweet_count = 0
    tweets_to_show = 10

    #show first 10 tweets
    for key in keys:
        if tweet_count < tweets_to_show:
            print(f"{key}: {db[key]}")
            tweet_count += 1
        else:
            break
    
    #while count of tweet smaller than overall tweets, allow uers to request show another 10 tweets
    while tweet_count < len(keys):
        show_more = input("Show more tweets (y/n)? > ")
        if show_more.lower() == "y":
            clear()
            for _ in range(tweets_to_show):
                if tweet_count < len(keys):
                    key = keys[tweet_count]
                    print(f"{key}: {db[key]}")
                    tweet_count += 1
            continue
        else:
            break

print("Your Tweeter")
while True:
    action = input("add or view tweets (a/v)? > ")
    if action == "a":
        add()
    else:
        view()