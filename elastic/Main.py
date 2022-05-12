from EsSearch import EsSearch


class Main:
    def __init__(self):
        self.es_search = EsSearch()

    def search(self, value):

        return self.es_search.search(value).get()

    def search_filtered(self, value):

        return self.es_search.search_filtered(value).get()

