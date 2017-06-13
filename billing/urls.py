from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^payment/product/(?P<product_id>[\d]+)\/?$', views.payment, name='billing_payment'),
    url(r'^payment/order/(?P<order_id>[\d]+)\/?$', views.payment_order, name='billing_payment_order'),
]
