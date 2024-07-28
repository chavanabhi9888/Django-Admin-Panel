from django.contrib import admin
from django.urls import path

from trainer.views import add_trainer, success_view, data_list_view
app_name='trainer'
urlpatterns = [
    path('add_trainer/', add_trainer, name= 'index'),
    path('added/', success_view, name='trainer'),
    path('trainers/', data_list_view, name='trainer_list')
]