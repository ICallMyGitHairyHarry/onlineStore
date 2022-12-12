# Generated by Django 3.2.16 on 2022-11-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('ingreds', models.TextField()),
                ('img', models.FilePathField()),
                ('pr_cost', models.PositiveSmallIntegerField()),
                ('pr_price', models.PositiveSmallIntegerField()),
                ('pr_left', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
