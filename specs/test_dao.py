from daos.dao import Dao

class TestDao:

    def __init__(self):
        self.dao = Dao('test_database')
        self.test_dao_instance()
        self.test_dao_wrong_instance()
        self.test_dao_create()
        self.test_dao_read()
    
    def test_dao_instance(self):
        assert isinstance(self.dao, Dao), f'{self.dao} is not a Dao instance'

    def test_dao_wrong_instance(self):
        assert not isinstance(self.dao, str), f'{self.dao} should be a Dao instance'

    def test_dao_create(self):
        result = self.dao.create()
        assert result == 'Created'

    def test_dao_read(self):
        result = self.dao.read()
        assert isinstance(result, list)