from Search import Search

class Main():
    @staticmethod
    def main():
        field = input("Search fiels: ")
        print(field)
        if field != 'exit' and field:
            value = input("Search value: ")
            search = Search()
            search.where(field, value)
            print(search.data)
            Main.main()
        




if __name__ == '__main__':
     Main.main()