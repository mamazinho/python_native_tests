class Dao:

    def __init__(self, file_name):
        super().__init__()
        self.__db_file = f'{file_name}'

    def create(self):
        with open(self.__db_file, 'a+') as _file:
            _file.write(f'{self}; \n')

        return 'Created'

    def read(self):
        with open(self.__db_file, 'r') as _file:
            all_items = _file.read()

        list_items = all_items.replace('\n', '').split(';')
        return list_items