# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-02 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_delete_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeOfCrop', models.IntegerField(choices=[(1, 'Wheat'), (2, 'Maize'), (3, 'Rice'), (4, 'Cane'), (5, 'Floor')], default='Wheat')),
            ],
        ),
    ]