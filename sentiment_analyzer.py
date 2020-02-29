from textblob import TextBlob

import re

class TweetAnalyzer():

	def cleanTweet(self, intweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", intweet).split())

	def sentimentAnalyzer(self, tweet):
