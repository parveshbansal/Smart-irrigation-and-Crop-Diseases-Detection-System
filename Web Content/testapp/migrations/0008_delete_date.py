# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-02 07:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Date',
        ),
    ]
