from daos.dao import Dao

class Product(Dao):

    def __init__(self, name, description, value):
        super().__init__('Products')
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f'{self.name} - {self.description} - {self.value}'

    @classmethod
    def read_all(cls):
        return Dao('Products').read()
        