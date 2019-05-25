#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Retrieving data from twitter with specific keyword and geo location by using Twython
import json
from twython import Twython

def retreive_data_kw(keyword):     #retreive data with specific keyword

    TWITTER_APP_KEY = '********'
    TWITTER_APP_KEY_SECRET ='****************'
    TWITTER_ACCESS_TOKEN = '*****************'
    TWITTER_ACCESS_TOKEN_SECRET = '***********'

    t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
    search = t.search(q=keyword,count=100)
    tweets = search['statuses']
    file = open("output.json", "w")
    for tweet in tweets:
        retweet=tweet['retweet_count']
        fav=tweet['favorite_count']
        screenname = "@" + tweet['user']['screen_name']
        id = tweet['id_str']
        text = tweet['text']
        date=tweet['created_at']
        data = { "id": id, "date":date, "name": screenname,"tweet": tweet['text'], "values":{"favorite":fav, "retweet": retweet}}
        print (json.dumps(data, indent=3, ensure_ascii=False)).encode('utf8')
        file.write(json.dumps(data, indent=3, ensure_ascii=False).encode('utf8'))

def retreive_data_geocode(geocode):     #retreive data with specific location

        TWITTER_APP_KEY = '********'
        TWITTER_APP_KEY_SECRET ='****************'
        TWITTER_ACCESS_TOKEN = '*****************'
        TWITTER_ACCESS_TOKEN_SECRET = '***********'

        t = Twython(app_key=TWITTER_APP_KEY,
                    app_secret=TWITTER_APP_KEY_SECRET,
                    oauth_token=TWITTER_ACCESS_TOKEN,
                    oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
        search = t.search(geocode=geocode, count=100)
        tweets = search['statuses']
        file = open("output.txt", "w")
        for tweet in tweets:
            retweet = tweet['retweet_count']
            fav = tweet['favorite_count']
            screenname = "@" + tweet['user']['screen_name']
            id = tweet['id_str']
            text = tweet['text']
            date = tweet['created_at']
            data = {"id": id, "date": date, "name": screenname, "tweet": tweet['text'],
                    "values": {"favorite": fav, "retweet": retweet}}
            print (json.dumps(data, indent=3, ensure_ascii=False)).encode('utf8')
            file.write(json.dumps(data, indent=3, ensure_ascii=False).encode('utf8'))

retreive_data_kw("YBU")
retreive_data_kw("#AYBU")
retreive_data_geocode('39.9708048,32.8187681,0.1mi')


