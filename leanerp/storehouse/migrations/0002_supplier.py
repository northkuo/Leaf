# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-03 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('internal_code', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('phone', models.TextField(blank=True)),
            ],
        ),
    ]
