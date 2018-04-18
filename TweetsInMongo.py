from pymongo import MongoClient
import json

import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import io
import os

start_time = time.time()


class listener(StreamListener):
    def __init__(self, start_time, time_limit=60):
        self.time = start_time
        self.limit = time_limit

    def on_data(self, data):
        client = MongoClient("mongodb://localhost")
        db = client.twitter_db
        collection = db.twitter_collection
        tweet = json.loads(data)

        collection.insert(tweet)

    def on_error(self, status):
        print status

