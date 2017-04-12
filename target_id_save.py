import math, re, command, config
from twitter_response import Response
from target_id import TargetId
from user import User

target_model = TargetId()
user_model = User()
users = user_model.select_user_ids()
user_ids = []
for user in users:
    user_ids.extend(list(user))
accounts = config.ACCOUNTS
for account in accounts:
    target_follow_ids = list(set(command.follow_ids(account)))
    for id in target_follow_ids:
        if id in user_ids:
            continue
        try:
            target_model.create(user_id=id)
        except:
            import traceback
            traceback.print_exc()
            continue
