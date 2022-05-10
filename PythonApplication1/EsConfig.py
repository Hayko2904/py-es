import http.client
import json
import requests


class EsConfig:
    def __init__(self):
        self.conn = http.client.HTTPConnection("192.155.88.66:9200")
        headers = {"Content-type": "application/json", "Accept": "text/plain"}

        self.data = {
            "query": {
                "bool": {
                    "must": []
                }
            }
        }
        self.conn.request("GET", '/lead/_search', json.dumps(self.data), headers)

    def get(self):
        res = self.conn.getresponse()
        data = res.read()
        self.conn.close()

        return data
