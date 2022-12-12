from django.db import models

from catalogue.models import Product
from registration.models import Customer, Adm


class Order(models.Model):
    ord_status = models.CharField(max_length=1, default='1')
    cr_date = models.DateTimeField()
    pay_date = models.DateTimeField(blank=True, null=True, default=None)
    full_pr = models.PositiveSmallIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Adm, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Prod_list(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pr_amount = models.PositiveSmallIntegerField()
