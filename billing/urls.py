from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^payment/product/(?P<product_id>[\d]+)\/?$', views.payment, name='billing_payment'),
    # compras
    url(r'^purchase/(?P<order_id>[\d]+)\/?$', views.item_purchase, name='item_purchase'),
    url(r'^purchases$', views.purchases, name='purchases'),

    # vendas
    # url(r'^sale/(?P<order_id>[\d]+)\/?$', views.item_sold, name='item_sold'),
    url(r'^sales$', views.sales, name='sales'),
]
