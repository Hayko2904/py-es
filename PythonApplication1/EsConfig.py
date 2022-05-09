import http.client
import json


class EsConfig():
    def __init__(self):
        self.conn = http.client.HTTPConnection("192.155.88.66:9200")
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        """
        data = {
          "query": {
            "match": {
              "Job_Number": searchText
            }
          }
}
        self.conn.request("GET", '/lead/_search', json.dumps(data), headers)
        test = self.conn.getresponse()

        print(test.read())

        conn.close()
        """
        





