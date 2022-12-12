from django.urls import path

from . import views

app_name = 'basket'
urlpatterns = [
    path('', views.basket, name='basket'),
    path('add_product/<str:product_id>', views.add_product, name='add_product'),
    path('subtract_product/<str:product_id>', views.subtract_product, name='subtract_product'),
    path('order', views.order, name='order'),
    path('create_order', views.create_order, name='create_order'),
]
