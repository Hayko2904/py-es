from EsConfig import EsConfig


class EsSearch(EsConfig):
    def __init__(self):
        super().__init__()

    def search(self, value: str = None) -> object:
        data = {
            "query_string": {
                "query": value
            }
        }

        self.data['query']['bool']['must'].append(data)

        return self
