import math, re, command, config
from twitter_response import Response
from user import User
from target_id import TargetId
import random
import logging
from datetime import datetime
import traceback
logging.basicConfig(filename='girl_save.log',level=logging.DEBUG)
logging.info('スタートします')
logging.info(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
user_model = User()
account = user_model.random_screen_name()
# account = random.choice(["otsumajoshi ‏", "gersbfh1 ‏", "new_GIOCATORE", "blue_re17 ‏", "nami10ve ‏", "shu_vivi1211 "])
logging.info("このアカウントのフォローを取得します %s" % account)
for account in account:
    account = account[0]
target_ids = command.follow_ids(account)
logging.info("target_ids")
users = user_model.select_user_ids()
user_ids = []
for user in users:
    user_ids.extend(list(user))
target_follow_lists = command.get_lookup(target_ids)
res = Response()
logging.info('取得したIDをループでまわす')
for list in target_follow_lists:
    res.user_information(list)
    logging.info(res.name)
    logging.info("screen_name: %s" % res.screen_name)
    if res.user_id in user_ids:
        logging.info("同じものです")
        continue    
    college = command.college_decision(res.description)
    if college == None:
        logging.info("大学生じゃない")
        continue
    if command.black_list_decision(res.name):
        logging.info("ブラックリストです")
        continue
    if res.follow_count > 1000:
        logging.info("フォローが多い")
        continue
    # one_week_second = 604800
    # today = int(datetime.now().strftime('%s'))
    # last_tweet_time = int(dateutil.parser.parse(status["created_at"]).strftime('%s'))
    # if (today - last_tweet_time) > one_week_second:
    #     continue
    logging.info('データを登録するよ %s' % res.name)
    try:
        user_model.create(name = res.name, user_id = res.user_id, screen_name = res.screen_name, follow_count = res.follow_count, follower_count = res.follower_count, follow_flg = res.follow_flg, follower_flg = res.follower_flg, url = res.url, college = college, description = res.description, protected = res.protected)
        logging.info("データ登録完了 %s" % res.name)
    except:
        traceback.print_exc()
        continue
