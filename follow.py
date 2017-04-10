import math, re, command
import twitter, config, database
from user import User

user_model = User()
result = user_model.where(column="follow_flg", value=0)
user_ids = list(result)
print(user_ids)
for user_id in user_ids:
    result = command.user_follow(user_id)
    if result == "break":
      break
    user_model.update(column="follow_flg", value=1, user=user_id)
