# Imports
import tweepy
import pandas as pd
from keys import *
import requests
import os.path
import time

## Twitter Roast Bot ##
# *This is the public branch version without keys and personal information*

# Get API keys from keys.py
client = tweepy.Client(bearer_token=bearer_token,
                       consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret,
                       return_type=requests.Response,
                       wait_on_rate_limit=True)
client2 = tweepy.Client(bearer_token=bearer_token)

# Funtions


def tweets_to_csv(user):
    # user -> str
    # Grabs 100 most recent tweets from a user, saves to csv, outputs file name
    aname = user.username
    if os.path.exists(csvpath + aname + ".csv"):
        print("Data already exists for account: " + aname)
        return (csvpath + aname + ".csv")
    # Define query
    query = 'from:' + aname

    # get max. 100 tweets
    tweets = client.search_recent_tweets(query=query,
                                         max_results=100)
    # Save data as dictionary
    tweets_dict = tweets.json()

    # Extract "data" value from dictionary
    tweets_data = tweets_dict['data']

    # Transform to pandas Dataframe
    df = pd.json_normalize(tweets_data)

    # save df to csv and return name
    df.to_csv(csvpath + aname + ".csv")
    print("Created new CSV for account: " + aname)
    return (csvpath + aname + ".csv")


def roast_by_name(name):
    # str -> str
    # Creates a roast if the the name contains keywords love or says
    uname = name
    kword = "Love "
    if kword in uname:
        lv = word_after(uname, kword)
        return ("Hey @" + user.username + " it's great and all that you love "
                + lv + ", but like I just chatted with your mom and she said"
                + " she would love if you could take a shower and move"
                + " our of her bacement 👵😡 💩🚿")
    kword = "says "
    if kword in uname:
        lv = word_after(uname, kword)
        return ("@" + user.username + " says "
                + lv + " more like " + user.username
                + "'s doctor says to loose some weight "
                + "👨‍⚕️🤷  🍕🤰🍩")
    else:
        # return an empty string if no keyword in the name
        return ""


def roast_by_bio(user):
    # user -> str
    # Returns custom roast if the bio contains certain words
    d = user.description
    if "NFT" in d:
        return ("Yo @" + user.username + " I dont even think I need to roast "
                + "you as you need to wake up every day living with your" +
                " terrible financial decision... Nobody cares about your jpg " +
                "so plz stop.PS. Bitcoin dropped 30 percent last week 😂😂")
    if "dog" in d:
        return ("@" + user.username + " you seem to REALLY like your dog... "
                + "Just becase you love dogs and not cats does not " +
                "exclude you from becoming a crazy lady. TBH you prob "
                + "feed your dog better food then your family 🐶😳")
    else:
        # If these words are not found return empty string
        return ""


def roast_by_hobby(hb, user):
    # str, user -> str
    # returns custom roast based on a users hobby
    if hb == "anime":
        return ("Lmaooooo get your weeb ass out of the bacement lol. The "
                + "The only reason @" + user.username + " likes 2d anime "
                + "girls is because all the real woman run away 🏃😢 😂😂😂")
    if hb == "gaming":
        return ("Real talk with @" + user.username + " now. I dont know how"
                + "your life became consisting of a bag of doritos and "
                + "fortnite but we can get you back on track. Call me back "
                + "after you shower, you can do it! 🙏😌")
    if hb == "Trump ":
        return ("Hey @" + user.username + " you kinda have a lil Trump "
                + "obsession... idk if you love or hate him but we can move"
                + " on now.... I dont care if he caused you HUGEEE issues "
                + "but go tell him on truth social 😂😂😂")
    if hb == "Biden":
        return ("Lmaoo @" + user.username + " you better not unironicly be "
                + "talking about boring ol politics on twitter. Lets talk about "
                + "how good ol joey cant ride a bike 🚴🤕 😂😂😂")
    if hb == "art ":
        return ("Yo @" + user.username + ' What sort of "art" are you looking '
                + "at 🤔... Arts cool and all but have you heard of grass? 🌾"
                + " The sun is also p dope as awell ☀️ "
                + "Give it a shot sometime!")
    if (hb == "football") or (hb == "baseball"):
        return ("Uhhh @" + user.username + " So your telling me you invite "
                + "guys over to your house and watch men play with balls "
                + 'all day 🤨  ...ok "bro" ')
    if hb == "reddit":
        return ("Do I actually need to roast @" + user.username + " man "
                + "deadass gets yelled at by his mom everyday to move out"
                + " of his house, shower, shave his neckbeard, and to not" +
                " wear the fedora 🤓🖥️ ...poor mom 👵")
    if hb == "food":
        return ("Ey yo @" + user.username + " I like food as well ya know but"
                + " how many calories did you say you were eating every "
                + "day 🤔 ...ok bro I will let your doctor talk to you "
                + "about your McHabits 🍟")
    if hb == "running":
        return ("The only reason @" + user.username + " runs is because "
                + "they were bullied in school... Just because you call it a "
                + '"hobby" now, it really is just the same thing lol 🏃 🤛😠')
    if hb == "meme":
        return ("Hey @" + user.username + " you do know people follow you "
                + "for the memes you steal not actually you, right? 🤷")
    else:
        # If user has no hobbies return a complement!
        return ("Good for you @" + user.username + "for not spending your "
                + "time on twitter. I donthave a roast for you! 😁 ... Or "
                + "you are just into uncommon hobbies 😳")


def word_after(s, keyword):
    # str, str -> str
    # Returns the word after keyword in a string
    sindex = s.find(keyword)
    return ((s[(len(keyword) + sindex):]).split())[0]


def tweets_to_hobby(csv):
    # str -> str
    # Returns the most frequent hobby word that appears in users tweets
    dic = {'Trump ': 0, 'Biden': 0, 'anime': 0, 'gaming': 0, 'art ': 0,
           'baseball': 0, 'football': 0, 'reddit': 0, 'meme': 0, 'running': 0, 'food': 0}
    with open(csv, 'r') as f:
        for line in f:
            for key in dic:
                if key in line:
                    dic[key] = dic.get(key, 0) + 1
    mostapp = max(dic, key=dic.get)
    print("Most Appeared is: " + mostapp)
    return mostapp


def roastme(user):
    # user -> str
    # Returns a custom roast of the specified user

    # First try to roast by name (most personal)
    nameroast = roast_by_name(user.name)
    if len(nameroast) > 1:
        return nameroast
    # Then try to roas by bio (less personal)
    bio_roast = roast_by_bio(user)
    if len(bio_roast) > 1:
        return bio_roast
    # Lastly roast their hobby
    else:
        path = tweets_to_csv(user)
        hobby = tweets_to_hobby(path)
        return roast_by_hobby(hobby, user)


# Main

# File paths
csvpath = "Tweet_Data/"
path_to_roast = "toroast.txt"

# Read the names to roast file and save the contents to a list removing the /n
with open(path_to_roast) as file:
    lines = file.readlines()
    accounts = [line.rstrip() for line in lines]
# Roast every account in the list
for account in accounts:
    print(account)
    # Convert the username given to a user that has username, name, description
    user = client2.get_user(username=account, user_fields=[
                            'name', "description"]).data
    print(user.name)
    # Roast user and save to string
    roast = roastme(user)
    # Tweet the roast
    client.create_tweet(text=roast)
    print("Roast", roast)
    # Wait for 4 seconds before roasting the next account to not get api banned
    time.sleep(4)
