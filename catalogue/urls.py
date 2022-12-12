from django.urls import path

from . import views

app_name = 'catalogue'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    # path('product/<int:pk>', views.ProductView.as_view(), name='product'),
    path('product/<int:product_id>', views.product, name='product'),
]
