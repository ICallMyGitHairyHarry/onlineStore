# Generated by Django 3.2.16 on 2022-11-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='', upload_to='products'),
        ),
    ]
