# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-07 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0006_auto_20171206_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nodule',
            name='case',
        ),
        migrations.RemoveField(
            model_name='nodule',
            name='centroid',
        ),
        migrations.AddField(
            model_name='candidate',
            name='added_by_hand',
            field=models.BooleanField(default=False),
        ),
    ]
