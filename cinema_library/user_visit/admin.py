from django.contrib import admin
from .models import UserVisit


# Register your models here.

@admin.register(UserVisit)
class UserVisitAdmin(admin.ModelAdmin):
    pass
