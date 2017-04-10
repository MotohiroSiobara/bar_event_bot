import math, re, command, config
from twitter_response import Response
from user import User

user_model = User()
users = user_model.select_user_ids()
user_ids = []
for user in users:
    user_ids.extend(list(user))
# my_follow_lists = command.follow_lists(config.MY_ACCOUNT)
accounts = config.ACCOUNTS
for account in accounts:
    target_follower_lists = command.follow_lists(account)
    print("my_follow_lists")
    for list in target_follower_lists:
            res = Response()
            res.user_information(list)
            print(res.name)
            if res.user_id in user_ids:
                continue
            college = command.college_decision(res.description)
            if college == None:
                break
            if not black_list_decision(res.name):
                break
            if res.follower_count > 800:
                break
            try:
                user_model.create(name = res.name, user_id = res.user_id, screen_name = res.screen_name, follow_count = res.follow_count, follower_count = res.follower_count, follow_flg = res.follow_flg, follower_flg = res.follower_flg, url = res.url, college = college, description = res.description)
            except:
                import traceback
                traceback.print_exc()
