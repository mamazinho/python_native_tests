from daos.dao import Dao
import pytest

class TestDao:

    def test_dao_instance(self):
        dao = Dao('test_database')
        assert isinstance(dao, Dao), f'{dao} is not a Dao instance'

    def test_dao_wrong_instance(self):
        dao = Dao('test_database')
        assert not isinstance(dao, str), f'{dao} should be a Dao instance'

    def test_dao_many_fields_in_instance(self):
        with pytest.raises(TypeError):
            Dao('test_database', 'mais um campo')

    def test_dao_create(self):
        dao = Dao('test_database')
        result = dao.create()
        assert result == 'Created'

    def test_dao_read(self):
        dao = Dao('test_database')
        result = dao.read()
        assert isinstance(result, list)