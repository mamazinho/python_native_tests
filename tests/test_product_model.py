from models.product import Product
import pytest

class TestProductModel:

    def test_product_instance(self):
        prod = Product('novo', 'novo prod', 20.20)
        assert isinstance(prod, Product), f'{prod} is not a Product instance'

    def test_product_wrong_instance(self):
        prod = Product('novo', 'novo prod', 20.20)
        assert not isinstance(prod, str), f'{prod} should be a Product instance'

    def test_dao_many_fields_in_instance(self):
        with pytest.raises(TypeError):
            Product('novo', 'novo prod', 20.20, 'mais um campo')

    def test_product_name_content(self):
        prod = Product('novo', 'novo prod', 20.20)
        assert prod.name == 'novo'

    def test_product_name_type(self):
        prod = Product('novo', 'novo prod', 20.20)
        assert isinstance(prod.name, str)

    def test_product_description_content(self):
        prod = Product('novo', 'novo prod', 20.20)
        assert prod.description == 'novo prod'

    def test_product_description_type(self):
        prod = Product('novo', 'novo prod', 20.20)
        assert isinstance(prod.description, str)

    def test_product_value_content(self):
        prod = Product('novo', 'novo prod', 20.20)
        assert prod.value == 20.20

    def test_product_value_type(self):
        prod = Product('novo', 'novo prod', 20.20)
        assert isinstance(prod.value, float)

    def test_product_create(self):
        prod = Product('novo', 'novo prod', 20.20)
        result = prod.create()
        assert result == 'Created'

    def test_product_read(self):
        result = Product.read_all()
        assert isinstance(result, list)