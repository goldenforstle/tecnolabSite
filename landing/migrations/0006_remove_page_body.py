# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-15 11:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_auto_20161115_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='body',
        ),
    ]
