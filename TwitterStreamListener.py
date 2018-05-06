import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import io
import os
import json

ckey = '*******************'
consumer_secret = '**************************************************'
access_token_key = '**********************************************'
access_token_secret = '*****************************************'

start_time = time.time() #grabs the System time
keyword_list = ['twitter']  #track list


class listener(StreamListener):
    def __init__(self, start_time, time_limit=60):

        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []

    def on_data(self, data):

        saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')

        while (time.time() - self.time) < self.limit:

            try:

                self.tweet_data.append(data)

                return True


            except BaseException, e:
                print 'failed ondata,', str(e)
                time.sleep(5)
                pass

        saveFile = io.open('raw_tweets.json', 'w', encoding='utf-8')
        saveFile.write(u'[\n')
        saveFile.write(','.join(self.tweet_data))
        saveFile.write(u'\n]')
        saveFile.close()
        exit()

    def on_error(self, status):

        print status

    def on_disconnect(self, notice):

        print 'bye'

start_time = time.time()

keyword_list = ['emoji']


auth = OAuthHandler(ckey, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

twitterStream = Stream(auth, listener(start_time, time_limit=200))
twitterStream.filter(track=keyword_list, languages=['en'])
