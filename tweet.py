import tweepy
import csv


class TwitterScrapper:
    def __init__(self):
        auth = tweepy.OAuthHandler("x7DvILXws4xwZRNVMToNp5tje", "nDL7SqsrZACzKTaIA3Ve4qNtTG5KcLAIXIridvPzFy27pBDSCK")
        auth.set_access_token('1603988101-qcdF7E3RPHBxh2Acukidtd2ofxIRyWFxW7bwM2g',
                              'Dfn9uUua9tZye2YZ1xF1XUVdCwve10IFpfvTqp7k9gWvH')
        self.api = tweepy.API(auth)

    def getTweets(self, keywords, csvFileName):
        csvFile = open(csvFileName, 'w')
        csvFile.truncate()
        csvWriter = csv.writer(csvFile)
        if not isinstance(keywords, list):
            keywords = [keywords]
        for keyword in keywords:
            for tweet in tweepy.Cursor(self.api.search, q=keyword, count=100, lang="en", since="2017-04-03").items():
                csvWriter.writerow([tweet.user.screen_name, tweet.created_at, tweet.text])
