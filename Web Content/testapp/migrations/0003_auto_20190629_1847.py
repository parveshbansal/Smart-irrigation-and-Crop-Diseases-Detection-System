# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-29 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20190629_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropdetail',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
