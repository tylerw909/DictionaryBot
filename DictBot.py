#!/usr/bin/python
import tweepy as twp
import time
import random
import requests
import json

# credentials to login to twitter api
consumer_key = 'nmkCn8VhDEDXOE1L8bH56z0T8'
consumer_secret = 'YOLwF6lSMjNnMykMHp6loIXAkNezeBfPAyLiLyAqRbO8CoeQsW'
access_token = '1104117265589522433-bDsWbAIhxt1zxWfZUrHH09vg79HDEy'
access_secret = 'osgL3bNwCo81APZyNyXOUfvSXAZq9xVBGZ8mXKKzXgqF2'

# credentials for oxford dictionary api
app_id = "c61f86ed"
app_key = "3619c026aab8720030520f80a85191be"
language = "en-gb"


# login to twitter account api
auth = twp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = twp.API(auth)


# loop through file with 466426 "words" (mostly words)
fp = open("words.txt", "r")
lines = fp.read().split()
total_words = 466426

while total_words > 1:
    num = random.randint(0,466425)
    next_word = lines[num]

    if next_word.isalpha():
        word_id = next_word
        url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
        req = requests.get(url, headers={"app_id": "c61f86ed", "app_key": "3619c026aab8720030520f80a85191be"})
        
        if req.status_code==200:
            try:
                word_id = word_id.capitalize()
                define = req.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
                grammar = req.json()['results'][0]['lexicalEntries'][0]['lexicalCategory']['text']
                new_post = "DictionaryBot's Word of the Hour!\n"+'\n'+word_id+'\n'+"Definition- "+define+'\n'+ "Part of speech- "+grammar
                api.update_status(new_post)
                print('Succesful posting!')
            except KeyError:
                continue
        else:
            print('ERROR OCCURED! Request status code: ' + str(req.status_code))
    
    time.sleep(2400)  # (2400) this number of seconds (~40min) that allows for 1000 requests per month if constantly running
    total_words -= 1   