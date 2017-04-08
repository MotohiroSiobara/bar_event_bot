import json, config, response
from requests_oauthlib import OAuth1Session
import re

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
    res = TWITTER.get(url, params = params)
    if res.status_code == 200:
      timeline = json.loads(res.text)
      for tweet in timeline:
        print(tweet['user']['name']+'::'+tweet['text'])
        print(tweet['created_at'])
        print('----------------------------------------------------')
    else:
      error = res_json["errors"][0]
      self.error_code_decision(error["code"])
      return []

  def get_follower_ids(self, name):
    ids = []
    cursor = None
    while True:
      url = "https://api.twitter.com/1.1/followers/ids.json"
      params = {
        'screen_name': name,
        'count': 5000,
        'cursor': cursor
      }
      res = self.twitter.get(url, params = params)
      res_json = json.loads(res.text)
      if res.status_code == 200:
        res_ids = res_json["ids"]
        cursor = res_json["next_cursor"]
        for id in res_ids:
          ids.append(id)
        if not cursor:
          break
      else:
        error = res_json["errors"][0]
        self.error_code_decision(error["code"])
        break
    return ids

  def follow(self, id):
    url = "https://api.twitter.com/1.1/friendships/create.json"
    params = {
      'user_id': id
    }
    res = self.twitter.post(url, params)
    res_json = json.loads(res.text)
    if res.status_code == 200:
      print("follow %s" % res_json["name"])
    else:
      error = res_json["errors"][0]
      print(error)
      self.error_code_decision(error["code"])
      if error["code"] == 161:
        return "break"
      else:
        return "error"

  def get_follow_ids(self, name):
    ids = []
    cursor = None
    while True:
      url = "https://api.twitter.com/1.1/friends/ids.json"
      params = {
        "screen_name": name,
        "count": 5000,
        "cursor": cursor
      }
      res = self.twitter.get(url, params = params)
      res_json = json.loads(res.text)
      if res.status_code == 200:
        res_ids = res_json["ids"]
        cursor = res_json["next_cursor"]
        for id in res_ids:
          ids.append(id)
        if not cursor:
          break
      else:
        error = res_json["errors"][0]
        self.error_code_decision(error["code"])
        print(error)
        break
    return ids
    print(ids)

  def send_direct_message(self, id, text):
    url = "https://api.twitter.com/1.1/direct_messages/new.json"
    params = {
      "user_id": id,
      "text": text
    }
    res = self.twitter.post(url, params)
    res_json = json.loads(res.text)
    if res.status_code == 200:
      print("%s さんに送信しました" % res_json["sender"]["name"])
    else:
      print(res_json["errors"][0])
      print("送信失敗")

  def error_code_decision(self, code):
    if code == 161:
      print("twitterの利用制限に達しました。明日再度実行してください")
    elif code == 88:
      print("15分以内に15件実行したためしばらくおまちください")
    elif code == 34:
      print("そのページは存在しません")
    elif code == 160:
      print("すでにリクエストを送信済みです")
    else:
      print("エラー %d" % code)

  def tweet(self, text):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = {
      "status": text
    }
    res = self.twitter.post(url, params = params)
    res_json = json.loads(res.text)
    if res.status_code == 200:
      print("text: %s" % res_json["text"])
    else:
      print(res_json["errors"][0])

  def get_followers_list(self, screen_name):
    cursor = None
    lists = []
    while True:
      url = "https://api.twitter.com/1.1/followers/list.json"
      params = {
        "screen_name": screen_name,
        "count": 200,
        "cursor": cursor
      }
      res = self.twitter.get(url, params = params)
      res_json = json.loads(res.text)
      if res.status_code == 200:
        for user in res_json["users"]:
          description = user["description"]
          for girl in self.girl_lists:
            if description.find(girl) > -1:
              lists.append(user["id"])
              break
        cursor = res_json["next_cursor"]
        if not cursor:
          break
      else:
        error = res_json["errors"][0]
        self.error_code_decision(error["code"])
        break
    return lists

  def unfollow(self, user_id):
    url = "https://api.twitter.com/1.1/friendships/destroy.json"
    params = {
      "user_id": user_id
    }
    res = self.twitter.post(url, params = params)
    res_json = json.loads(res.text)
    if res.status_code == 200:
      print("名前: %s" % res_json["name"])
    else:
      print(res_json["errors"][0])

  def get_lookup(self, ids):
    url = "https://api.twitter.com/1.1/users/lookup.json"
    params = {
      "user_id": ids
    }
    res = self.twitter.get(url, params = params)
    res_json = json.loads(res.text)
    if res.status_code == 200:
      return res_json
    else:
      error = res_json["errors"][0]
      self.error_code_decision(error["code"])
      return []
