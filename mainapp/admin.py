from django.contrib import admin
from .models import *


@admin.register(HexData)
class HexData(admin.ModelAdmin):
    pass


@admin.register(Hypothesis)
class Hypothesis(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'birth_date']
    list_select_related = ['user']
    list_per_page = 10
    ordering = ['user__first_name', 'user__last_name', 'birth_date']
    search_fields = ['first_name__istartswith', 'last_name_istartswith']