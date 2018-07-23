from django.contrib import admin
from .models import CanDo, CanGet, DishType
# Register your models here.


class CanDoAdmin(admin.ModelAdmin):
    """ admin of CanDo"""
    search_fields = ['name']


class CanGetAdmin(admin.ModelAdmin):
    """ admin of CanGet"""
    list_display = ('name', 'cal')
    search_fields = ['name']

admin.site.register(CanDo, CanDoAdmin)
admin.site.register(CanGet, CanGetAdmin)
admin.site.register(DishType)
