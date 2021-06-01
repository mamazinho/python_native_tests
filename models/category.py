from daos.dao import Dao

class Category(Dao):

    def __init__(self, name, description):
        super().__init__('Categories')
        self.name = name
        self.description = description
    
    def __str__(self):
        return f'{self.name} - {self.description}'

    @classmethod
    def read_all(cls):
        return Dao('Categories').read()