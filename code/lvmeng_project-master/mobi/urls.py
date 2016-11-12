#coding:utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^product_detail/$', views.Product_Detail),
    url(r'^news_detail/$', views.News_Detail),

]
