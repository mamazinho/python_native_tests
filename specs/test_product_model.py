from models.product import Product

class TestProductModel:

    def __init__(self):
        self.prod = Product('novo', 'novo prod', 20.20)
        self.test_product_instance()
        self.test_product_wrong_instance()
        self.test_product_name_content()
        self.test_product_name_type()
        self.test_product_description_content()
        self.test_product_description_type()
        self.test_product_value_content()
        self.test_product_value_type()
        self.test_product_create()
        self.test_product_read()
    
    def test_product_instance(self):
        assert isinstance(self.prod, Product), f'{self.prod} is not a Product instance'

    def test_product_wrong_instance(self):
        assert not isinstance(self.prod, str), f'{self.prod} should be a Product instance'

    def test_product_name_content(self):
        assert self.prod.name == 'novo'

    def test_product_name_type(self):
        assert isinstance(self.prod.name, str)

    def test_product_description_content(self):
        assert self.prod.description == 'novo prod'

    def test_product_description_type(self):
        assert isinstance(self.prod.description, str)

    def test_product_value_content(self):
        assert self.prod.value == 20.20

    def test_product_value_type(self):
        assert isinstance(self.prod.value, float)

    def test_product_create(self):
        result = self.prod.create()
        assert result == 'Created'

    def test_product_read(self):
        result = Product.read_all()
        assert isinstance(result, list)