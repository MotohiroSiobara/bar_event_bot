import math, re, command
import twitter, config, database
from user import User

user_model = User()
result = user_model.where(column="follow_flg", value=0)
user_ids = list(result)
for user_id in user_ids:
    command.user_follow(user_id)
    user_model.update(column="follow_flg", value=1, user=user_id)
# twitter = twitter.TwitterBot()
# engine = database.ENGINE
# result = engine.execute('SELECT user_id FROM user WHERE follow_flg=0')

# for r in result:
#   user_id = r["user_id"]
#   result = twitter.follow(user_id)
#   if result == "break":
#     break
#   elif result == "followed":
#     print("check")
#   elif result == "error":
#     continue
#   engine.execute('UPDATE user SET follow_flg=1 WHERE user_id=%s', user_id)
