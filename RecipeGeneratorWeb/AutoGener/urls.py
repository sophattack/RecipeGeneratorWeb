from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'AutoGener'
urlpatterns = [
    path('', views.index, name='index'),
    path('dish/', views.get_dish, name='dish')
]
