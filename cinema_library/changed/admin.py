from django.contrib import admin
from .models import ChangeLog


# Register your models here.


@admin.register(ChangeLog)
class ChangeLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'data_create']
    list_filter = ['model', 'action', 'data_create', 'user']

