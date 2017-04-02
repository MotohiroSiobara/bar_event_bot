import json, config
from requests_oauthlib import OAuth1Session

class TwitterBot:
  def __init__(self):
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    self.twitter = OAuth1Session(CK, CS, AT, ATS)

  def get_tweets(self):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params ={
    'count': 5
    }
    res = self.twitter.get(url, params = params)
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

  def get_followers(self, name):
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

  def follow(self, ids):
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
      self.error_code_decision(error["code"])
      if error["code"] == 161:
        return "break"

  def get_follows(self, name):
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
    else:
      print("エラー %d" % code)

print("start")
twitter = TwitterBot()
# twitter.get_tweets()
ids = twitter.get_follows("otsumauniv2017")
print("ids")
my_follow_ids = twitter.get_follows("student_bar_")
print("my_follow_ids")
my_follower_ids = twitter.get_followers("student_bar_")
print("my_follwer_ids")
for id in ids:
  if (id in my_follow_ids):
    continue
  result = twitter.follow(id)
  if result == "break":
    break
for id in my_follower_ids:
  twitter.send_direct_message(id, "フォローありがとうございます！4月29日に新歓やるのですが参加しませんか？(°▽°)")
