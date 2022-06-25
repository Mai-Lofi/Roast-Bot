# Imports
import tweepy
import pandas as pd
from keys import *
import requests
import os.path
import time

#Import UserRoast class
from userroast import UserRoast

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

    #First create UserRoast object
    usr_rst = UserRoast(user.name, user.username, user.description)

    # First try to roast by name (most personal)
    nameroast = UserRoast.roast_by_name(usr_rst)
    if len(nameroast) > 1:
        return nameroast
    # Then try to roas by bio (less personal)
    bio_roast = UserRoast.roast_by_bio(usr_rst)
    if len(bio_roast) > 1:
        return bio_roast
    # Lastly roast their hobby
    else:
        path = tweets_to_csv(user)
        hobby = tweets_to_hobby(path)
        return UserRoast.roast_by_hobby(hobby, usr_rst)


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
