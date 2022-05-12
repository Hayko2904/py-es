import http.client
import json

from decouple import config


class EsConfig:
    def __init__(self):
        self.conn = http.client.HTTPConnection(config('ES_HOST'))

        self.data = {
            "size": 5000,
            "query": {
                "bool": {
                    "must": []
                }
            }
        }

    def get(self):
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        self.conn.request("GET", '/lead/_search', json.dumps(self.data), headers)
        res = self.conn.getresponse()
        data = res.read()
        self.conn.close()

        return data
