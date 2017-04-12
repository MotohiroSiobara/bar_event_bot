import math, re, command, config
from twitter_response import Response
from user import User
from target_id import TargetId

account = "Mariboo0107"
user_model = User()
target_ids = list(command.follow_ids(account))
users = user_model.select_user_ids()
user_ids = []
for user in users:
    user_ids.extend(list(user))
accounts = config.ACCOUNTS
target_follow_lists = command.get_lookup(target_ids)
res = Response()
for list in target_follow_lists:
    res.user_information(list)
    if res.user_id in user_ids:
        continue
    print(res.description)
    college = command.college_decision(res.description)
    if college == None:
        continue
    if command.black_list_decision(res.name):
        continue
    if res.follow_count > 800:
        continue
    print("res.name")
    try:
        user_model.create(name = res.name, user_id = res.user_id, screen_name = res.screen_name, follow_count = res.follow_count, follower_count = res.follower_count, follow_flg = res.follow_flg, follower_flg = res.follower_flg, url = res.url, college = college, description = res.description)
    except:
        import traceback
        traceback.print_exc()
        continue
