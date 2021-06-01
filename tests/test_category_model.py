from models.category import Category

class TestCategoryModel:

    def __init__(self):
        self.cat = Category('nova', 'nova cat')
        # This is not used here because types has no difference
        # self.wrong_cat = Category(2, 'nova cat') 
        self.test_category_instance()
        self.test_category_wrong_instance()
        self.test_category_name_content()
        self.test_category_name_type()
        self.test_category_description_content()
        self.test_category_description_type()
        self.test_category_create()
        self.test_category_read()
    
    def test_category_instance(self):
        assert isinstance(self.cat, Category), f'{self.cat} is not a Category instance'

    def test_category_wrong_instance(self):
        assert not isinstance(self.cat, str), f'{self.cat} should be a Category instance'

    def test_category_name_content(self):
        assert self.cat.name == 'nova'

    def test_category_name_type(self):
        assert isinstance(self.cat.name, str)

    def test_category_description_content(self):
        assert self.cat.description == 'nova cat'

    def test_category_description_type(self):
        assert isinstance(self.cat.description, str)

    def test_category_create(self):
        result = self.cat.create()
        assert result == 'Created'

    def test_category_read(self):
        result = Category.read_all()
        assert isinstance(result, list)