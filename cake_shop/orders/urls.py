from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
]