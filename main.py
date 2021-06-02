from models.category import Category
from models.product import Product
from specs.test_category_model import TestCategoryModel
from specs.test_product_model import TestProductModel
from specs.test_dao import TestDao

class Main:

    def __init__(self):
        # self.create_product()
        # self.read_product()
        # self.create_category()
        # self.read_category()
        TestCategoryModel()
        TestProductModel()
        TestDao()

    def create_product(self):
        prod = Product('novo', 'novo prod', 20.20)
        prod.create()

    def read_product(self):
        Product.read_all()

    def create_category(self):
        cat = Category('nova', 'nova cat')
        cat.create()
    
    def read_category(self):
        Category.read_all()

if __name__ == '__main__':
    Main()