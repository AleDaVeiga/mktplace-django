from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^my_ads$', views.my_ads, name='my_ads'),
    url(r'^product/(?P<id>[\d]+)\/?$', views.product_show, name='product_show'),
    url(r'^product/edit/(?P<product_id>[\d]+)\/?$', views.product_edit, name='product_edit'),
    url(r'^product/new$', views.product_new, name='product_new'),
]
