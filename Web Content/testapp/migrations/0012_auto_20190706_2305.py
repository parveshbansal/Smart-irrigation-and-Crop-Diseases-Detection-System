# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-06 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0011_userphone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userphone',
            old_name='username',
            new_name='username1',
        ),
    ]
