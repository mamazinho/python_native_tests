from models.category import Category
import pytest

class TestCategoryModel:
    
    def test_category_instance(self):
        cat = Category('nova', 'nova cat')
        assert isinstance(cat, Category), f'{cat} is not a Category instance'

    def test_category_wrong_instance(self):
        cat = Category('nova', 'nova cat')
        assert not isinstance(cat, str), f'{cat} should be a Category instance'

    def test_category_many_fields_in_instance(self):
        with pytest.raises(TypeError):
            Category('nova', 'nova cat', 'mais um campo')

    def test_category_name_content(self):
        cat = Category('nova', 'nova cat')
        assert cat.name == 'nova'

    def test_category_name_type(self):
        cat = Category('nova', 'nova cat')
        assert isinstance(cat.name, str)

    def test_category_description_content(self):
        cat = Category('nova', 'nova cat')
        assert cat.description == 'nova cat'

    def test_category_description_type(self):
        cat = Category('nova', 'nova cat')
        assert isinstance(cat.description, str)

    def test_category_create(self):
        cat = Category('nova', 'nova cat')
        result = cat.create()
        assert result == 'Created'

    def test_category_read(self):
        result = Category.read_all()
        assert isinstance(result, list)