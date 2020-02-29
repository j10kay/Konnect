from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
import re


class TweetAnalyzer(): # Function to clean tweets and remove
    def __init__(self):
        pass

    def cleanTweet(self, intweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", intweet).split())

    def sentimentAnalyzer(self, csvFileName = "myTweets.csv"): # Analyzes result from csv file
        analysis = SentimentIntensityAnalyzer()
        cur_tweets = self.listOfTweets(csvFileName)
        frating = 0
        count = 0

        for tweet in cur_tweets:
            vs = analysis.polarity_scores(tweet)
            crating = (vs['compound'] + 1) * (5/2)
            frating += crating
            count += 1

        return frating/count

    def listOfTweets(self, csvFileName):
        with open(csvFileName) as csvfile:
            readCSV = csv.reader(csvfile, delimiter = ",")
            cur_tweets = []

            for row in readCSV:
                init_tweet = row[2]
                cur_tweets.append(init_tweet)

            i = 0
            while i < len(cur_tweets):
                temp = cur_tweets[i]
                cur_tweets[i] = temp[2:len(temp)-1]
                i += 1

        return cur_tweets
