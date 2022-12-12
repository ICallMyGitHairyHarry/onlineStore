from django.db import models

from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    district = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house = models.PositiveSmallIntegerField(blank=True, null=True)
    corp = models.PositiveSmallIntegerField()
    flat = models.PositiveSmallIntegerField()
    p_index = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username


class Adm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    u_role = models.CharField(max_length=1)

    def __str__(self):
        return self.user.username
