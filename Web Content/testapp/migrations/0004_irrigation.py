# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-30 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20190629_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='irrigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CropStage', models.IntegerField(choices=[(1, '1ststage'), (2, '2ndstage'), (3, '3rdstage'), (4, '4thstage'), (5, '5thstage')], default='1ststage')),
            ],
        ),
    ]