import http.client
import json


class EsConfig:
    def __init__(self):
        self.conn = http.client.HTTPConnection("192.155.88.66:9200")

        self.data = {
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
