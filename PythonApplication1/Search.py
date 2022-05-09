from EsSearch import EsSearch

class Search():
    data = {
        "query": {}
        }
    def __init__(self):
        self.search = EsSearch()

    @classmethod
    def where(cls, field, value):
        ee = []
        ee.append({field:value})
        print(ee)
        return cls



