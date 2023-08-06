from requests_oauthlib import OAuth1Session
import tweepy
import os
import json
from time import sleep
import requests
from Funcs import *
from datetime import datetime
from threading import Thread
from datetime import datetime, date, timedelta
import mysql.connector

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
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class retweet_follow(Thread):
    def run(self):
        mydb = mysql.connector.connect(
            host="localhost", user="admin", password="admin", database="bot"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM follow")
        myresult = mycursor.fetchall()
        arr = []
        arr.append(i[0] for i in myresult)
        while True:
            for i in arr:
                data = api.user_timeline(
                    i, count=1, include_rts=False, exclude_replies=True
                )
            sleep(60)


class retweet_search(Thread):
    def run(self):
        while True:
            now = datetime.utcnow() - timedelta(minutes=5)
            format = "%Y-%m-%dT%H:%M:%SZ"
            start = now.strftime(format)
            print("Searching for tweets all over Twitter")
            str = json.loads(
                client.search_recent_tweets(query=query_params, start_time=start)
            )
            arr = []
            for set in str.data:
                arr.append([set.text, set.id])
            for i in arr:
                print("Checking tweets to see if it meets the requirement for retweet")
                if check(i[0], criteria) == True:
                    print("Retweet")
                    client.retweet(i[1])
            sleep(900)


def check(input, criteria):
    count = 0
    arr = input.split(" ")
    inp = criteria.split(" ")
    for i in arr:
        if i in inp:
            count += 1
    if count > criteria:
        return True
    return False


def main():
    retweet_follow().start()
    retweet_search().start()


if __name__ == "__main__":
    main()
