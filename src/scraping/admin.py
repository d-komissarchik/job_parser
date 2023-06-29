from django.contrib import admin
from .models import City, Language, Vacancy, Error


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'city', 'language', 'timestamp']


@admin.register(Error)
class ErrorAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'data']
