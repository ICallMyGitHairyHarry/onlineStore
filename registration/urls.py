from django.urls import path

from . import views

app_name = 'registration'
urlpatterns = [
    path('logging', views.logging, name='logging'),
    path('registration', views.registration, name='registration'),
    path('user_creating', views.user_creating, name='user_creating'),
    path('registration_success', views.registration_success, name='registration_success'),
]
