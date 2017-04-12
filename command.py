import math, re, command
import config, database
from twitter import TwitterBot

twitter = TwitterBot()
my_account = config.MY_ACCOUNT

def follow_ids(screen_name):
    my_follow_ids = []
    cursor = ""
    while True:
        response = twitter.get_friends_ids(screen_name, cursor)
        if "error" in response:
            break
        else:
            ids = list(set(response["ids"]))
            my_follow_ids.extend(ids)
        cursor = next_cursor(response)
        if cursor == None:
            break
    return my_follow_ids


def get_lookup(ids):
    user_lists = []
    count = math.ceil(len(ids) / 100)
    for i in range(count):
        if i == 0:
            target_ids = ids[:100]
        else:
            i = (i + 1) * 100
            target_ids = ids[i - 100: i]
        response = twitter.get_lookup(target_ids)
        if "error" in response:
            break
        else:
            user_lists.extend(response)
    return user_lists

def follow_lists(screen_name):
    my_follow_lists = []
    cursor = ""
    while True:
        response = twitter.get_friends_lists(screen_name, cursor)
        if "error" in response:
            break
        else:
            my_follow_lists.extend(response["users"])
        cursor = next_cursor(response)
        if cursor == None:
            break
    return my_follow_lists

def user_follow(user_id):
    response = twitter.follow(user_id)
    if "error" in response:
        print(response["error"])
        code = response["error"]["code"]
        if code == 161:
            return "break"
    return "ok"

def next_cursor(response):
    if len(response["next_cursor_str"]) > 0:
        return response["next_cursor_str"]
    else:
        return  None

def college_decision(description):
    college = None
    for girl in config.GIRL_LISTS:
        if description.find(girl) > -1:
            college = college_name_string(girl)
            break
    return college

def black_list_decision(name):
    flg = False
    for list in config.BLACK_LIST:
        if name.find(list) > -1:
            flg = True
            break
    return flg

def college_name_string(college):
    if college == "owu":
        return "大妻"
    elif college == "jwu":
        return "実践"
    elif college == "kwu":
        return "共立"
    elif college == "ush":
        return "聖心"
    elif college == "kwu":
        return "家政"
    elif college == "jwu":
        return "東京女"
    elif college == "fri":
        return "フェリス"
    elif college == "agwjc":
        return "青短"
    elif college == "swu":
        return "昭和女"
    elif college == "gwc":
        return "学女"
    elif college == "swu":
        return "相模"
    elif college == "atm":
        return "跡見"
    elif college == "sgu":
        return "白梅"
    elif college == "sfu":
        return "聖徳"
    elif college == "jwu":
        return "十文字"
    elif college == "wjc":
        return "立短"
    else:
        return college
