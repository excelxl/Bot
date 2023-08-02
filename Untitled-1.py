from requests_oauthlib import OAuth1Session
import tweepy
import os
import json
from time import sleep
import requests
from Funcs import *


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

def main():
    with open(r"C:\Users\white\Documents\Bot\config.json") as json_file:
        data = json.load(json_file)
    api_key = data["API_KEY"]
    api_secret = data["API_SECRET"]

    bearer_token = data["BEARER_TOKEN"]

    access_token = data["ACCESS_TOKEN"]
    access_token_secret = data["ACCESS_TOKEN_SECRET"]

    query_params = data["QUERY"]
    criteria = data["CRITERIA"]

    client = tweepy.Client(
        bearer_token, api_key, api_secret, access_token, access_token_secret
    )

    auth = tweepy.OAuth1UserHandler(
        api_key, api_secret, access_token, access_token_secret
    )

    api = tweepy.API(auth)
    while True:
        str = json.loads(client.search_recent_tweets(query=query_params))
        arr = []
        for set in str:
            arr.append([set["text"], set["id"]])
        for i in arr:
            if check(i["text"], criteria) == True:
                client.retweet(i["id"])


if __name__ == "__main__":
    main()
