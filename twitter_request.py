from twitter_response import Response
class Request:
    def __init__(self, twitter):
        self.client = twitter

    def get(self, url, params = ""):
        json = self.client.get(url, params = params)
        res = Response()
        return res.response_json(json)

    def post(self, url, params):
        json = self.client.post(url, params = params)
        res = Response()
        return res.response_json(json)
