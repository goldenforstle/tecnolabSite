# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-01 07:49
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0003_auto_20160901_0558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='croppingthumb',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='slidepage',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='slider',
        ),
        migrations.AlterField(
            model_name='slider',
            name='croppingslide',
            field=image_cropping.fields.ImageRatioField('image', '1140x487', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='slider'),
        ),
    ]
