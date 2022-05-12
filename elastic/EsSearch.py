import json

from EsConfig import EsConfig


class EsSearch(EsConfig):
    def __init__(self):
        super().__init__()

    def search(self, value: str = None) -> object:
        data = {
            "query_string": {
                "query": value if value is not None else {}
            }
        }

        self.data['query']['bool']['must'].append(data)

        return self

    def search_filtered(self, data):
        self.data.update(json.loads(data))

        return self

