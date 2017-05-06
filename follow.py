import math, re, command
import twitter, config, database
from user import User
import logging
from datetime import datetime
import traceback
logging.basicConfig(filename='follow.log',level=logging.DEBUG)
logging.info('スタートします')
logging.info(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
my_friend_counts = command.my_friend_counts()
if my_friend_counts < 1800: 
  user_model = User()
  result = user_model.where(column="follow_flg", value=0)
  user_ids = list(result)
  for user_id in user_ids:    
      result = command.user_follow(user_id)
      if result == "break":
        logging.info("フォロー制限です")
        break
      logging.info("フォローしました")
      user_model.update(column="follow_flg", value=1, user=user_id)
else:
    logging.info("人数制限です")
