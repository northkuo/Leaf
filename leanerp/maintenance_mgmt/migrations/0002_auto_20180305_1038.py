# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-05 02:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storehouse.Store'),
        ),
    ]
