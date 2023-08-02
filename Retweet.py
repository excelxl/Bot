import tweepy
import time

api_key = "IIiL0NwPBOUH2IesaWhGLmOjW"
api_secret = "JanHT5j4LR7PHOAISWOdxcaO8zNhD4ISyk4yOWaO0VyTpejNAD"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAPDqowEAAAAAxAacEArn6CWtdZw%2Fa3kbhQ42ZDA%3DhPnBiAAtRjiDVvHLPXVjANcZO2QX2KK3rOMRWpI1TIpBf7IbCW"
access_token = "1683294496384258048-ZFL4rIMQ06tly7kWD6GpqqhpGDDug8"
access_token_secret = "TbdQm1TkKT30CgszvIsEuzn0AaERZL1z2gn8la5QOYWMq"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        
        try:
            client.retweet(tweet.id)
        
        except Exception as error:
            print(error)

stream = MyStream(bearer_token = bearer_token)

rule = tweepy.StreamRule("(Virat Kohli)(-is:retweet -is:reply)" )

stream.add_rules(rule)

stream.filter()