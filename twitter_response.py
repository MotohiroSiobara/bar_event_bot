import json, re
class Response:
    def __init__(self):
        pass

    def response_json(self, res):
        res_json = json.loads(res.text)
        if res.status_code == 200:
            return res_json
        else:
            error = res_json["errors"][0]
            print(error)
            return { "error": error }

    # テーブル作成用のデータを整形する
    def user_information(self,json):
        self.name = re.sub("[^\\u0000-\\uFFFF]", "(絵)", (json["name"]))
        self.user_id = str(json["id"])
        self.screen_name = json["screen_name"]
        self.follow_count = json["friends_count"]
        self.follower_count = json["followers_count"]
        self.follow_flg = 0
        self.follower_flg = 0
        self.url = json["url"]
        self.description = re.sub("[^\\u0000-\\uFFFF]", "(絵)", (json["description"]))
        self.college = ""
