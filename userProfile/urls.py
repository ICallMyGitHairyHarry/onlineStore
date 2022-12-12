from django.urls import path

from . import views

app_name = 'userProfile'
urlpatterns = [
    path('', views.user_profile, name='userProfile'),
    path('new_product', views.new_product, name='new_product'),
    path('product_created', views.product_created, name='product_created'),
    path('change_product', views.change_product, name='change_product'),
    path('delete_product/<int:product_id>', views.del_product, name='del_product'),
    path('modify_product/<int:product_id>', views.modify_product, name='modify_product'),
    path('product_modified/<int:product_id>', views.product_modified, name='product_modified'),
    path('change_status', views.change_status, name='change_status'),
    path('change_order_status_paid/<int:order_id>', views.change_order_status_paid, name='change_order_status_paid'),
    path('change_order_status_unpaid/<int:order_id>', views.change_order_status_unpaid,
         name='change_order_status_unpaid'),
]
