from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.URLField(default=False, max_length=2100)
    month_offer = models.BooleanField(default=False)
    availability = models.BooleanField(default=False)
    pickup = models.BooleanField(default=False)
    content = models.TextField(blank=True)
    price = models.DecimalField(default=True, max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

