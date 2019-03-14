from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stock_form', views.stock_form, name='stock_form'),
]
