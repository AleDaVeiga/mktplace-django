from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^payment/product/(?P<product_id>[\d]+)\/?$', views.payment, name='billing_payment'),
]
