import math, re, command, config
from twitter_response import Response
from user import User

user_model = User()
users = user_model.select_user_ids()
user_ids = []
for user in users:
    user_ids.extend(list(user))
my_follow_lists = command.follow_lists(config.MY_ACCOUNT)
print("my_follow_lists")
for list in my_follow_lists:
        res = Response()
        res.user_information(list)
        print(res.name)
        if res.user_id in user_ids:
            continue
        college = res.college
        for girl in config.GIRL_LISTS:
            if res.description.find(girl) > -1:
              college = girl
              break
        user_model.create(name = res.name, user_id = res.user_id, screen_name = res.screen_name, follow_count = res.follow_count, follower_count = res.follower_count, follow_flg = res.follow_flg, follower_flg = res.follower_flg, url = res.url, college = college, description = res.description)

# for r in result:
#     user_id = r["user_id"]
#     my_data_users.append(user_id)

# my_account = config.MY_ACCOUNT
# accounts = config.ACCOUNTS
# twitter = twitter.TwitterBot()
# my_follow_ids = twitter.get_follow_ids(my_account)
# print("my_follow_ids")
# my_follower_ids = twitter.get_follower_ids(my_account)
# print("my_follwer_ids")
# for account in accounts:
#     print(account)
#     user_ids = twitter.get_follower_ids(account)
#     # sum_of_sets = set(user_ids) - set(my_follow_ids)
#     # sum_of_lists = list(sum_of_sets)
#     target_ids = []
#     for id in user_ids:
#         if not id in my_follow_ids:
#             target_ids.append(id)
#     print(len(target_ids))
#     count = math.ceil(len(target_ids) / 100)
#     print(count)
#     ins = "INSERT INTO user (name, user_id, screen_name, follow_count, follower_count, follow_flg, follower_flg, url, college, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     for i in range(count):
#         if i == 0:
#             ids = target_ids[:100]
#         else:
#             i = (i + 1) * 100
#             ids = target_ids[i - 100: i]
#             lists = twitter.get_lookup(ids)
#             print(len(lists))
#             for list in lists:
#                 try:
#                     name = re.sub("[^\\u0000-\\uFFFF]", "(絵)", (list["name"]))
#                     user_id = str(list["id"])
#                     if user_id in my_data_users:
#                         continue
#                     screen_name = list["screen_name"]
#                     follow_count = list["friends_count"]
#                     follower_count = list["followers_count"]
#                     follow_flg = 0
#                     follower_flg = 0
#                     url = list["url"]
#                     description = re.sub("[^\\u0000-\\uFFFF]", "(絵)", (list["description"]))
#                     flg = ""
#                     for girl in config.GIRL_LISTS:
#                         if description.find(girl) > -1:
#                           flg = girl
#                           break
#                     if len(flg) > 0:
#                         engine.execute(ins, name, user_id, screen_name, follow_count, follower_count, follow_flg, follower_flg, url, flg, description)
#                 except:
#                     continue
