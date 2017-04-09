import json, config
from twitter_request import Request
from requests_oauthlib import OAuth1Session

class TwitterBot:
    def __init__(self):
        CK = config.CONSUMER_KEY
        CS = config.CONSUMER_SECRET
        AT = config.ACCESS_TOKEN
        ATS = config.ACCESS_TOKEN_SECRET
        self.twitter = OAuth1Session(CK, CS, AT, ATS)
        GIRL_LISTS = config.GIRL_LISTS
        ACCOUNTS = config.ACCOUNTS

    def get_tweets(self):
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
        params ={
            'count': 5
        }
        req = Request(self.twitter)
        return req.get(url, params)

    def get_follower(self, name):
        url = "https://api.twitter.com/1.1/followers/ids.json"
        params = {
          'screen_name': name,
          'count': 5000,
          'cursor': cursor
        }
        req = Request(self.twitter)
        return  req.get(url, params)

    def follow(self, id):
        url = "https://api.twitter.com/1.1/friendships/create.json"
        params = {
            'user_id': id
        }
        req = Request(self.twitter)
        return  req.post(url, params)

    def get_friends_ids(self, name, cursor = ""):
        url = "https://api.twitter.com/1.1/friends/ids.json"
        params = {
          "screen_name": name,
          "count": 5000,
          "cursor": cursor
        }
        req = Request(self.twitter)
        return  req.get(url, params)

    def get_followers_list(self, screen_name):
        url = "https://api.twitter.com/1.1/followers/list.json"
        params = {
          "screen_name": screen_name,
          "count": 200,
          "cursor": cursor
        }
        req = Request(self.twitter)
        return  req.get(url, params)

    def get_friends_lists(self, screen_name, cursor):
        url = "https://api.twitter.com/1.1/friends/list.json"
        params = {
          "screen_name": screen_name,
          "count": 200,
          "cursor": cursor
        }
        req = Request(self.twitter)
        return  req.get(url, params)

    def unfollow(self, user_id):
        url = "https://api.twitter.com/1.1/friendships/destroy.json"
        params = {
            "user_id": user_id
        }
        req = Request(self.twitter)
        return  req.post(url, params)

    def get_lookup(self, ids):
        url = "https://api.twitter.com/1.1/users/lookup.json"
        params = {
          "user_id": ids
        }
        req = Request(self.twitter)
        return  req.get(url, params)
