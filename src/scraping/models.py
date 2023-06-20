from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Назва мiста', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Населений пункт'
        verbose_name_plural = 'Населені пункти'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Мова програмування', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Мова програмування'
        verbose_name_plural = 'Мови програмування'

    def __str__(self):
        return self.name
