import database

class TargetId():
    def __init__(self):
        self.engine = database.ENGINE

    def create(self, **kwargs):
        user_id = kwargs["user_id"]
        query = "INSERT INTO target_id (user_id) VALUES (%s)"
        self.engine.execute(query, user_id)

    def select_user_ids(self):
        return self.engine.execute('SELECT user_id FROM target_id')
