from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^my_ads$', views.my_ads, name='my_ads'),
    url(r'^product/edit/(?P<product_id>[\d]+)\/?$', views.product_edit, name='product_edit'),
    url(r'^product/new\/?$', views.product_new, name='product_new'),
    url(r'^product/delete/(?P<product_id>[\d]+)\/?$', views.product_delete, name='product_delete'),
]