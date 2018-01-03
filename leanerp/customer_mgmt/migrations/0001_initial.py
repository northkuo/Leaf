# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-03 07:32
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VIPCard',
            fields=[
                ('card_id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('points', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('points_last_update_date', models.DateTimeField(default=datetime.datetime(1900, 1, 1, 0, 0))),
            ],
        ),
        migrations.CreateModel(
            name='VIPMember',
            fields=[
                ('member_id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime(1900, 1, 1, 0, 0))),
            ],
        ),
        migrations.AddField(
            model_name='vipcard',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_mgmt.VIPMember'),
        ),
    ]
