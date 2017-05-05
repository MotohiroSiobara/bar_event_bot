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
        protected = kwargs["protected"]
        query = "INSERT INTO user (name, user_id, screen_name, follow_count, follower_count, follow_flg, follower_flg, url, college, description, protected) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.engine.execute(query, name, user_id, screen_name, follow_count, follower_count, follow_flg, follower_flg, url, college, description, protected)

    def select_user_ids(self):
        return self.engine.execute('SELECT user_id FROM user')

    def where(self, column, value):
        if column == "follow_flg":
            return self.engine.execute('SELECT user_id FROM user WHERE follow_flg=?', value)
    def update(self, column, value, user):
        if column == "follow_flg":
            return self.engine.execute('UPDATE user SET follow_flg=1 WHERE user_id=?', user)
    def random_screen_name(self):
        return self.engine.execute('SELECT screen_name FROM user WHERE protected=0 ORDER BY RANDOM() LIMIT 1')
    
 
