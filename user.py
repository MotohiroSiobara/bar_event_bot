import database

class User():
    def __init__(self):
        self.engine = database.ENGINE

    def create(self, **kwargs):
        name = kwargs["name"]
        user_id = kwargs["user_id"]
        screen_name = kwargs["screen_name"]
        follow_count = kwargs["follow_count"]
        follwer_count = kwargs["follower_count"]
        follow_flg = kwargs["follow_flg"]
        follwer_flg = kwargs["follower_flg"]
        url = kwargs["url"]
        college = kwargs["college"]
        description = kwargs["description"]
        query = "INSERT INTO user (name, user_id, screen_name, follow_count, follower_count, follow_flg, follower_flg, url, college, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.engine.execute(query, self.name, self.user_id, self.screen_name, self.follow_count, self.follower_count, self.follow_flg, self.follower_flg, self.url, self.college, self.description)

    def select_user_ids(self):
        return self.engine.execute('SELECT user_id FROM user')
