# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
    ]