import tweepy
import csv

auth = tweepy.OAuthHandler("x7DvILXws4xwZRNVMToNp5tje", "nDL7SqsrZACzKTaIA3Ve4qNtTG5KcLAIXIridvPzFy27pBDSCK")
auth.set_access_token('1603988101-qcdF7E3RPHBxh2Acukidtd2ofxIRyWFxW7bwM2g', 'Dfn9uUua9tZye2YZ1xF1XUVdCwve10IFpfvTqp7k9gWvH')
api = tweepy.API(auth)

csvFile = open('myTweets.csv', 'w')
csvFile.truncate()
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, q="#RateBlack", count=100, lang="en", since="2017-04-03").items():
    csvWriter.writerow([tweet.user.screen_name, tweet.created_at, tweet.text.encode('utf-8')])
