# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_160', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='summarymodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='summarymodel',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
