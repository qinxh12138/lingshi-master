# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-15 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_shopcar_is_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcar',
            name='order',
            field=models.ForeignKey(db_column='oid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.Order', verbose_name='商品ID'),
        ),
    ]