from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^my_ads$', views.my_ads, name='my_ads'),
    url(r'^my_data$', views.my_data, name='my_data'),
    url(r'^busca\/$', views.search, name='portal_search'),

    # questions
    url(r'^product/(?P<product_id>[\d]+)/questions/(?P<question_id>[\d]+)/answer/(?P<answer_id>[\d]+)/edit\/?$', views.product_answer_question_edit, name='product_answer_question_edit'),
    url(r'^product/(?P<product_id>[\d]+)/questions/(?P<question_id>[\d]+)/answer/new\/?$', views.answer_question_new, name='answer_question_new'),
    url(r'^product/(?P<product_id>[\d]+)/questions/(?P<question_id>[\d]+)\/?$', views.product_answer_question, name='product_answer_question'),
    url(r'^product/(?P<product_id>[\d]+)/questions\/?$', views.product_question, name='product_question'),
    url(r'^product/(?P<product_id>[\d]+)/list/questions\/?$', views.product_list_questions, name='product_list_questions'),


    url(r'^product/new/question/(?P<product_id>[\d]+)\/?$', views.product_new_question, name='product_new_question'),
    url(r'^product/new$', views.product_new, name='product_new'),
    url(r'^product/edit/(?P<product_id>[\d]+)\/?$', views.product_edit, name='product_edit'),
    url(r'^product/(?P<slug>[-\w\d]+)\/?$', views.product_show, name='product_show'),
]
