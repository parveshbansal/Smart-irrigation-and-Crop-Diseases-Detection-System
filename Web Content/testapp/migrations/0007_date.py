# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-02 07:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20190701_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
    ]