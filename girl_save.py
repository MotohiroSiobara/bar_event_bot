import math, re, command, config
from twitter_response import Response
from user import User
from target_id import TargetId
import random
# from datetime import datetime
# from datetime import datetime, timedelta
# import dateutil.parser

accounts = ["naphat31", "Rm_ozk5 ‏", "hk1220__ ‏", "_____yui0_____ ‏", "tnyt_98 ‏"]
account = random.choice(accounts)
user_model = User()
target_ids = command.follow_ids(account)
print(target_ids)
users = user_model.select_user_ids()
print("users")
user_ids = []
for user in users:
    user_ids.extend(list(user))
accounts = config.ACCOUNTS
target_follow_lists = command.get_lookup(target_ids)
res = Response()
for list in target_follow_lists:
    print("res.name")
    res.user_information(list)
    if res.user_id in user_ids:
        continue
    college = command.college_decision(res.description)
    if college == None:
        continue
    if command.black_list_decision(res.name):
        continue
    if res.follow_count > 800:
        continue
    # one_week_second = 604800
    # today = int(datetime.now().strftime('%s'))
    # last_tweet_time = int(dateutil.parser.parse(status["created_at"]).strftime('%s'))
    # if (today - last_tweet_time) > one_week_second:
    #     continue
    try:
        user_model.create(name = res.name, user_id = res.user_id, screen_name = res.screen_name, follow_count = res.follow_count, follower_count = res.follower_count, follow_flg = res.follow_flg, follower_flg = res.follower_flg, url = res.url, college = college, description = res.description)
    except:
        import traceback
        traceback.print_exc()
        continue
