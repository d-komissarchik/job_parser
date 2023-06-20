from django.contrib import admin
from .models import City, Language


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']