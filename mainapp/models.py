from django.db import models
from django.conf import settings
from django.contrib import admin


class HexData(models.Model):
    source = models.CharField(max_length=255)
    from_number = models.IntegerField()
    to_number = models.IntegerField()
    hexdatastring = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self) -> str:
        return f'hex_data_id={self.id}'


class Hypothesis(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    lat_long_field = models.JSONField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'hypo_id={self.id}'

    class Meta:
        ordering = ['name']


class Profile(models.Model):
    address = models.CharField(max_length=255)
    birth_date = models.DateField()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
