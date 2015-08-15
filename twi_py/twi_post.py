#!/usr/bin/python
# -*- coding: utf-8 -*-

from auth_sga import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET
#sga_auth には、上の4つの情報が入っています
import tweepy
import time

#oauth認証
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#post関数
def post(post_word):
    if post_word == "time":
        api.update_status(status = time.ctime())    
        return 1
    elif post_word == "exit":
        return -1
    else:
        api.update_status(status = post_word)
        return 1
def main():
    try:
        print("input post words")
        post_word = input()
        t = post(post_word)

        if t == 1:
            print("tweet success")
        elif t == -1:
            print("exit success")
        else:
            print("undefined error.")
        
    except KeyboardInterrupt:
        print("\nexit: KeyboardInterrupt")
        exit

if __name__ == "__main__":
    main()
    
