#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import tweepy
from tweepy import Stream, TweepError
import logging
import urllib
import time
from sga_auth import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET

#oauth認証
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#ふぁぼる単語リスト
fav_words = ["てすと", "test", "ふぁぼ"]

class CustomStreamListener(tweepy.StreamListener):

    #こいつでふぁぼります
    def fav(self,status,fav_words):
        for word in fav_words :
            if status.text.find(word) != -1 :
                api.create_favorite(status.id)
                print("success favorite:")
                print("@"+ status.author.screen_name + status.text + "\n")
                return True
        return False
    
    def on_status(self, status):
        try:
            self.fav(status,fav_words)
        except Exception as e:
            print ('Encountered Exception:' + e, file=sys.stderr)
            pass
    
    def on_error(self, status_code):
        print ("Encountered error with status code:" + status_code,file=sys.stderr)
        return True # Don't kill the stream
    
    def on_timeout(self):
        print ('Timeout...' ,file=sys.stderr)
        return True # Don't kill the stream

            
def main():
    try:
        stream = Stream(auth, CustomStreamListener())
        stream.timeout = None

        #userstreamの開始
        print("start")
        stream.userstream()
    except KeyboardInterrupt :
        print("\nexit: KeyboardInterrupt")
        return
    
if __name__ == "__main__":
    main()
