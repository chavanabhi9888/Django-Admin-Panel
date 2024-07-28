from django.contrib import admin
from django.urls import path

from gym.views import addgym, success_view, data_list_view
app_name='gym'
urlpatterns = [
    path('form/', addgym, name= 'index'),
    path('success/', success_view, name='success'),
    path('data/', data_list_view, name='gym_list')
]