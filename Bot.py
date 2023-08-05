from requests_oauthlib import OAuth1Session
import tweepy
import os
import json
from time import sleep
import requests
from Funcs import *
from datetime import datetime

with open(r"C:\Users\white\Documents\Bot\config.json") as json_file:
    data = json.load(json_file)
api_key = data["API_KEY"]
api_secret = data["API_SECRET"]
bearer_token = data["BEARER_TOKEN"]
access_token = data["ACCESS_TOKEN"]
access_token_secret = data["ACCESS_TOKEN_SECRET"]
query_params = data["QUERY"]
criteria = data["CRITERIA"]
time = int(data["TIME"])
sleep = data["SLEEP"]
client = tweepy.Client(
    bearer_token, api_key, api_secret, access_token, access_token_secret
)


def check(input, criteria):
    count = 0
    arr = input.split(" ")
    f = open("input.txt", "r")
    inp = f.read()
    for i in arr:
        if i in inp:
            count += 1
    if count > criteria:
        return True
    return False


def retweet_follow():
    print()


def retweet_search():
    print()


def main():
    while True:
        now = datetime.now()
        time = now.strftime("%H")
        if time == sleep:
            sleep(60 * 120)
        print("Searching for tweets all over Twitter")
        str = json.loads(
            client.search_recent_tweets(query=query_params, start_time="12:00:01")
        )
        arr = []
        for set in str:
            arr.append([set["text"], set["id"]])
        for i in arr:
            print("Checking tweets to see if it meets the requirement for retweet")
            if check(i["text"], criteria) == True:
                print("Retweet")
                client.retweet(i["id"])
        print("Getting tweets from following people")
        str = json.loads(client.get_home_timeline())
        for set in str:
            arr.append([set["text"], set["id"]])
        for i in arr:
            print("Checking if their tweets meets the requirements")
            if check(i["text"], criteria) == True:
                print("Retweet")
                client.retweet(i["id"])
        sleep(time)


if __name__ == "__main__":
    main()