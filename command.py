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
        if response == None:
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
        lists = twitter.get_lookup(target_ids)
        user_lists.extend(lists)
    return user_lists

def follow_lists(screen_name):
    my_follow_lists = []
    cursor = ""
    while True:
        response = twitter.get_friends_lists(screen_name, cursor)
        if response == None:
            break
        else:
            my_follow_lists.extend(response["users"])
        cursor = next_cursor(response)
        if cursor == None:
            break
    return my_follow_lists

def next_cursor(response):
    if len(response["next_cursor_str"]) > 0:
        return response["next_cursor_str"]
    else:
        return  None
