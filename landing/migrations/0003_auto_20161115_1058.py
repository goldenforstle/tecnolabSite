# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-15 10:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20161115_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='didascalia',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='didascalia_uk',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='link',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='scritta',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='scritta_uk',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='slider',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='titolo_uk',
        ),
    ]
