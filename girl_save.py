import math, re
import twitter, config, database

my_account = config.MY_ACCOUNT
accounts = config.ACCOUNTS
twitter = twitter.TwitterBot()
my_follow_ids = twitter.get_follow_ids(my_account)
print("my_follow_ids")
my_follower_ids = twitter.get_follower_ids(my_account)
print("my_follwer_ids")
for account in accounts:
    print(account)
    user_ids = twitter.get_follower_ids(account)
    # sum_of_sets = set(user_ids) - set(my_follow_ids)
    # sum_of_lists = list(sum_of_sets)
    target_ids = []
    for id in user_ids:
        if not id in my_follow_ids:
            target_ids.append(id)
    print(len(target_ids))
    count = math.ceil(len(target_ids) / 100)
    print(count)
    for i in range(count):
        if i == 0:
            ids = target_ids[:100]
        else:
            i = (i + 1) * 100
            ids = target_ids[i - 100: i]
            lists = twitter.get_lookup(ids)
            engine = database.ENGINE
            ins = "INSERT INTO user (name, user_id, screen_name, follow_count, follower_count, follow_flg, follower_flg, url, college, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            print(len(lists))
            for list in lists:
                name = re.sub("[^\\u0000-\\uFFFF]", "(絵)", (list["name"]))
                user_id = str(list["id"])
                result = engine.execute('SELECT user_id FROM user WHERE user_id=%s', user_id)
                print(result)
                if result:
                    continue
                screen_name = list["screen_name"]
                follow_count = list["friends_count"]
                follower_count = list["followers_count"]
                follow_flg = 0
                follower_flg = 0
                url = list["url"]
                description = re.sub("[^\\u0000-\\uFFFF]", "(絵)", (list["description"]))
                flg = ""
                for girl in config.GIRL_LISTS:
                    if description.find(girl) > -1:
                      flg = girl
                      break
                if len(flg) > 0:
                    engine.execute(ins, name, user_id, screen_name, follow_count, follower_count, follow_flg, follower_flg, url, flg, description)