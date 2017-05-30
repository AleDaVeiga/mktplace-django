from django.db.models import Q

from portal.models import Product


class ProductRepository:
    def search_products(self, search=""):
        if search:
            products = Product.objects.filter(status='Active')\
                                      .filter((Q(name__icontains=search) | Q(description__icontains=search)))
            if products:
                return products
            return None