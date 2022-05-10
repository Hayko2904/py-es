from EsSearch import EsSearch

class Main:
    def es(self, value):
        search = EsSearch()

        return search.search(value).get()


