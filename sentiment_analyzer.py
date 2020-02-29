from textblob import TextBlob

import re

class TweetAnalyzer():

	def cleanTweet(self, intweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", intweet).split())

	def sentimentAnalyzer(self, tweet):
		trating = (analysis.sentiment.polarity + 1) * 5/2

		srating = 5 - analysis.sentiment.subjectivity

		frating = trating + srating

		return frating

def GetAndUpdateRating(tweet):
	with open('mytweet.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter = ",")

		cur_tweets = []

		for row in readCSV:
			init_tweet = row[2]
