from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'AutoGener'
urlpatterns = [
    path(r'dish/delete/<name>', views.dish_delete, name='dish_delete'),
    path('dish/list_remove/<name>', views.dish_list_remove, name='dish_list_remove'),
    path('dish/addtype/', views.add_type, name="add_type"),
    path('dish/type_delete/<name>', views.type_delete, name='type_delete'),
    path('detail/<name>', views.get_dish_detail, name='dish_detail'),
    path(r'ingredient/<name>', views.ingre_delete, name='ingre_delete'),
    path('schedule/', views.get_scehdele, name='schedule'),
    path('dish/', views.get_dish, name='dish'),
    path('ingredient/', views.get_ingredient, name='ingredient')
]
