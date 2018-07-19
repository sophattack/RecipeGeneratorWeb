from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'AutoGener'
urlpatterns = [
    path(r'dish/(?P<name>[a-z]$', views.dish_delete, name='dish_delete'),
    path(r'ingredient/(?P<name>[a-z]$', views.ingre_delete, name='ingre_delete'),
    path('schedule/', views.get_scehdele, name='schedule'),
    path('', views.index, name='index'),
    path('dish/', views.get_dish, name='dish'),
    path('ingredient/', views.get_ingredient, name='ingredient')
]
