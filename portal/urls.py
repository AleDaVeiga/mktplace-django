from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^my_ads$', views.my_ads, name='my_ads'),
    url(r'^my_data$', views.my_data, name='my_data'),
    url(r'^product/search$', views.product_search, name='product_search'),
    url(r'^product/new/question/(?P<product_id>[\d]+)\/?$', views.product_question, name='product_question'),
    url(r'^product/new$', views.product_new, name='product_new'),
    url(r'^product/edit/(?P<product_id>[\d]+)\/?$', views.product_edit, name='product_edit'),
    url(r'^product/(?P<slug>[-\w\d]+)\/?$', views.product_show, name='product_show'),
]
