# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-09 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_framework', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
