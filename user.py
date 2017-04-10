import database

class User():
    def __init__(self):
        self.engine = database.ENGINE

    def create(self, **kwargs):
        name = kwargs["name"]
        user_id = kwargs["user_id"]
        screen_name = kwargs["screen_name"]
        follow_count = kwargs["follow_count"]
        follower_count = kwargs["follower_count"]
        follow_flg = kwargs["follow_flg"]
        follower_flg = kwargs["follower_flg"]
        url = kwargs["url"]
        college = kwargs["college"]
        description = kwargs["description"]
        query = "INSERT INTO user (name, user_id, screen_name, follow_count, follower_count, follow_flg, follower_flg, url, college, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.engine.execute(query, name, user_id, screen_name, follow_count, follower_count, follow_flg, follower_flg, url, college, description)

    def select_user_ids(self):
        return self.engine.execute('SELECT user_id FROM user')
