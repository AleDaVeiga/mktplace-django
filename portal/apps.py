from django.apps import AppConfig
import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex


class PortalConfig(AppConfig):
    name = 'portal'

    def ready(self):
        Product = self.get_model('Product')
        algoliasearch.register(Product, ProductIndex)
        # Category = self.get_model('Category')
        # algoliasearch.register(Category, CategoryIndex)


class ProductIndex(AlgoliaIndex):
    fields = ('id', 'name', 'short_description', 'description', 'slug',)
    settings = {'searchableAttributes': ['name', 'description']}
    index_name = 'product_index'


# class CategoryIndex(AlgoliaIndex):
#     fields = ('id', 'name', 'slug', 'categories',)
#     settings = {'searchableAttributes': ['name']}
#     index_name = 'category_index'
