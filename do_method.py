import json

import requests


class ReUilt:

    def __init__(self, Url, ApiKey):
        self.url = Url
        self.apikey = ApiKey

    def do_go(self, param, mode):
        if mode is None:
            url = self.url + '?param=' + param
        else:
            url = self.url + '?param=' + param + '&mode=' + str(mode)
        return requests.get(url=url, headers={'Api-Key': '...'}).json()

    def do_post(self, data, mode):
        header = {
            "content-type": "application/json",
            'Api-Key': self.apikey
        }
        if data is None:
            data = {
                "params": [data]
            }
        elif mode is None:
            data = {
                "params": data.strip(',').split(',')
            }
        else:
            data = {
                "params": data.strip(',').split(','),
                "mode": mode
            }
        url = self.url + 's'
        print(data)
        return requests.post(url=url, headers=header, data=json.dumps(data)).json()


if __name__ == '__main__':
    ReUilt().do_post([''])
