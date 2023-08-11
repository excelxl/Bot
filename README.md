# Bot
CONFIG FILE:
API_KEY: AKA consumer key of company's twitter account
API_SECRET: AKA consumer key secret of company's twitter account
ACCESS_TOKEN: access token of company's twitter account
ACCESS_TOKEN_SECRET: access token secret of company's twitter account
BEARER_TOKEN: bearer token of company's twitter account
QUERY: query of twitter search function, input whatever you want twitter search function to find
CRITERIA: % of keywords that appears in the found tweets when using search function
TIME_S: time to sleep after retweeting found tweets 
TIME_F: time to sleep after retweeting following people's tweets
DB_HOST: company's database hosting address
DB_USER: user login credential for database
DB_PASSWORD: password login credential for database
DB_NAME: database name
PATH: path to look for images when tweeting company's posts

GUIDE to creating directories in the PATH folder:
When you insert a row into the POSTS table in the BOT databse, you'll also assign an id to the post
Create a folder with the id of the post you want to include the images in
Copy your images inside that folder with the id name, maximum 4 images per post

Hashtag file: insert hashtags you want to search and scan posts with, one hastag per line
