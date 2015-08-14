#!/usr/bin/python
# -*- coding: utf-8 -*-

from sga_auth import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET
#sga_auth には、上の4つの情報が入っています
import tweepy
import time

#oauth認証
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#post
api.update_status(status = time.ctime())    
