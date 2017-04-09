import math, re
import twitter, config, database

twitter = twitter.TwitterBot()
engine = database.ENGINE
result = engine.execute('SELECT user_id FROM user WHERE follow_flg=0')

for r in result:
  user_id = r["user_id"]
  result = twitter.follow(user_id)
  if result == "break":
    break
  elif result == "followed":
    print("check")
  elif result == "error":
    continue
  engine.execute('UPDATE user SET follow_flg=1 WHERE user_id=%s', user_id)
