#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import tweepy
from tweepy import Stream, TweepError
import logging
import urllib
import time
from auth_sga import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET

#oauth認証
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# pythonにおいて、
#  class hoge(parent):
# は、parentの継承を意味する。

class CustomStreamListener(tweepy.StreamListener):
    
    def on_status(self, status):
        try:
            #取得したついっとの出力
            print ("---" + status.author.screen_name +"---")
            print (status.text)
        except Exception as e:
            print ('Encountered Exception:' + e, file=sys.stderr)
            pass
    
    def on_error(self, status_code):
        print ("Encountered error with status code:" + status_code,file=sys.stderr)
        return True # Don't kill the stream
    
    def on_timeout(self):
        print ('Timeout...' ,file=sys.stderr)
        return True # Don't kill the stream
            
class UserStream(Stream):

    def user_stream(self, follow=None, track=None, async=False, locations=None):
        self.parameters = {"delimited" : "length", }
        self.headers['Content-type'] = "application/x-www-form-urlencoded"
        
        if self.running:
            raise TweepError('Stream object already connected!')
            
        self.scheme = "https"
        self.host = 'userstream.twitter.com'
        self.url = '/2/user.json'

        ##コメントの部分はよくわからないのでコメントアウト
        # #パラメータの追加
        # if follow:
        #     #もし、"follow"リストが空でなかったら、それらを全部str型にしてパラメータに追加
        #     self.parameters['follow'] = ','.join(map(str, follow))

        # if track:
        #     self.parameters['track'] = ','.join(map(str, track))
        # if locations and len(locations) > 0:
        #     assert len(locations) % 4 == 0
        #     self.parameters['locations'] = ','.join(['%.2f' % l for l in locations])

            
        self.body = urllib.parse.urlencode(self.parameters)
        logging.debug("[ User Stream URL ]: %s://%s%s" % (self.scheme, self.host, self.url))
        logging.debug("[ Request Body ] :" + self.body)

        #UserStreamの開始
        print("start")
        self._start(async)
        
def main():
    #インスタンスの生成。
    #詳しくは、https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.pyのソースを見てください。
    stream = UserStream(auth, CustomStreamListener())

    stream.timeout = None
    
    #userstreamの取得.Streamクラスには、本来userstremがあるが、今回はオリジナルのuser_streamを呼びだしている。
    try:
        stream.user_stream()
    except KeyboardInterrupt :
        print("\nexit: KeyboardInterrupt")
        exit
if __name__ == "__main__":
    main()
