import requests
import json


class Talk:
    def __init__(self):
        self.key = 'DZZWB7icwGDrSRPCFDp2UBsBAavlDxop'
        self.api = 'https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk'

    def get(self, talking):
        url = self.api
        r = requests.post(url, {'apikey': self.key, 'query': talking})
        data = json.loads(r.text)
        if data['status'] == 0:
            t = data['results']
            ret = t[0]['reply']
        else:
            ret = '・・・・・・・・・'
        return ret
