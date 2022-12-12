from django.db import models


class Product(models.Model):
    pr_name = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)
    ingreds = models.TextField()
    img = models.ImageField(upload_to='products', default="", blank=True, null=True)
    pr_cost = models.PositiveSmallIntegerField()
    pr_price = models.PositiveSmallIntegerField()
    pr_left = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.pr_name
