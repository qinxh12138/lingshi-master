# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-12 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcar',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
