# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-05 01:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventorycheck', '0002_clerkmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clerk',
            name='real_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
