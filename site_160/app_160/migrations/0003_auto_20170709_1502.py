# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 13:02
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_160', '0002_auto_20170705_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summarymodel',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=10),
        ),
    ]