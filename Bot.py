import time
from requests_oauthlib import OAuth1Session
import tweepy
import os
import json
from time import sleep
import requests
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
times = int(data["TIME_S"])
timef = int(data["TIME_F"])
db_host = data["DB_HOST"]
db_user = data["DB_USER"]
db_password = data["DB_PASSWORD"]
db_name = data["DB_NAME"]
path = data["PATH"]
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search=open("sample_search.txt",)
searchr=json.load(search)
follow=open("sample_response.txt")
followr=json.load(follow)

class retweet_follow(Thread):
    def run(self):
        mydb = mysql.connector.connect(
            host=db_host, user=db_user, password=db_password, database=db_name
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM follow")
        myresult = mycursor.fetchall()
        arr = []
        arr.append([i[0], i[1]] for i in myresult)
        curr_time = time.strftime("%H", time.localtime())
        while curr_time != "17" and curr_time != "18":
            for i in arr:
                #arr = json.loads(api.user_timeline(i[0], count=10, include_rts=False, exclude_replies=True))
                arr=followr
                for tweet in arr:
                    hash = tweet["entities"]["hashtags"]
                    if tweet["id"] != i[1]:
                        if check(hash):
                            api.retweet(tweet["id"])
            sleep(timef)


class retweet_search(Thread):
    def run(self):
        curr_time = time.strftime("%H", time.localtime())
        while curr_time != "17" and curr_time != "18":
            now = datetime.utcnow() - timedelta(minutes=15)
            format = "%Y-%m-%dT%H:%M:%SZ"
            start = now.strftime(format)
            print("Searching for tweets all over Twitter")
            #arr = json.loads(api.search_tweets(query=query_params, start_time=start))
            arr=searchr
            for i in arr["statuses"]:
                hash = i["entities"]["hashtags"]
                print("Checking tweets to see if it meets the requirement for retweet")
                if check(hash) == True:
                    print("Retweet")
                    api.retweet(i["id"])
            sleep(times)


class post_stuff(Thread):
    def run(self):
        mydb = mysql.connector.connect(
            host=db_host, user=db_user, password=db_password, database=db_name
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM schedule;")
        myresult = mycursor.fetchall()
        timetable = []
        timetable.append(i[0] for i in myresult)
        currtime = time.strftime("%H", time.localtime())
        while currtime != "17" and curr_time != "18":
            curr_time = time.strftime("%H:%M:%S", time.localtime())
            if curr_time in timetable:
                mycursor.execute("SELECT * FROM posts ORDER BY id DESC LIMIT 1;")
                myresult = mycursor.fetchone()
                arr = []
                arr.append([i[0], i[1]] for i in myresult)
                files = os.listdir(path+"/"+arr[0][0])
                media=[]
                for i in len(files):
                    media.append(api.media_upload(path+"/"+arr[0][0]+"/"+i))
                api.update_status(arr[0][1],media=media)



def check(input):
    with open("hashtags.txt") as file:
        lines = [line.rstrip() for line in file]
    count = 0
    arr = lines.split(" ")
    inp = input.split(" ")
    for i in arr:
        if i in inp:
            count += 1
    if count > criteria:
        return True
    return False


def main():
    retweet_follow().start()
    retweet_search().start()
    post_stuff().start()


if __name__ == "__main__":
    main()
