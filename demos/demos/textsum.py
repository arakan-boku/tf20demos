import requests
import json


class TextSummarize:
    def __init__(self):
        self.key = 'DZZL4YgS8jq9DrHhtCOeuCMh27ssQ9s8'
        self.api = 'https://api.a3rt.recruit-tech.co.jp/text_summarization/v1'

    def get(self, inputtext):
        url = self.api
        quoted_text = inputtext
        print(quoted_text)
        r = requests.post(url,
                          {'apikey': self.key,
                           'sentences': quoted_text,
                           'linenumber': 1,
                           'separation': '。'})
        data = json.loads(r.text)
        if data['status'] == 0:
            ret = data['summary']
        else:
            ret = ['サマリが取得できませんでした。']
        return ret
