from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('list',views.list_products,name='list'),
    path('detail',views.detail_products,name='detail'),
]