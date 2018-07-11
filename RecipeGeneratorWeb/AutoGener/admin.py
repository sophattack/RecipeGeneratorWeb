from django.contrib import admin
from .models import CanDo, CanGet
# Register your models here.


class CanDoAdmin(admin.ModelAdmin):
    """ admin of CanDo"""
    list_display = ('name', 'type')
    search_fields = ['name']


class CanGetAdmin(admin.ModelAdmin):
    """ admin of CanGet"""
    list_display = ('name', 'price', 'cal')
    search_fields = ['name']

admin.site.register(CanDo, CanDoAdmin)
admin.site.register(CanGet, CanGetAdmin)
