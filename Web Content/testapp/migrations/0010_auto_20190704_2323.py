# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-04 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0009_croptype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='croptype',
            name='TypeOfCrop',
            field=models.IntegerField(choices=[(1, 'Wheat'), (2, 'Ground Nuts'), (3, 'Garden flowers'), (4, 'Maize'), (5, 'Paddy'), (6, 'Potato'), (7, 'pulse'), (8, 'SugerCane'), (9, 'coffee')], default='Wheat'),
        ),
    ]
