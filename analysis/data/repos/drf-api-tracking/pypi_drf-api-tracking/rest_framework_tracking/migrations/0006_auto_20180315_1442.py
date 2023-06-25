# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-15 14:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rest_framework_tracking", "0005_auto_20171219_1537"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apirequestlog",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
