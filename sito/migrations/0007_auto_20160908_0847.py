# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-08 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0006_auto_20160901_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fiere',
            name='croppingcarousel',
        ),
        migrations.RemoveField(
            model_name='fiere',
            name='croppingrender',
        ),
        migrations.RemoveField(
            model_name='fiere',
            name='croppingslide',
        ),
        migrations.RemoveField(
            model_name='fiere',
            name='croppingthumb',
        ),
        migrations.RemoveField(
            model_name='fiere',
            name='designbig',
        ),
        migrations.RemoveField(
            model_name='fiere',
            name='designnews',
        ),
        migrations.RemoveField(
            model_name='fiere',
            name='designthumb',
        ),
        migrations.RemoveField(
            model_name='fiere',
            name='slidepage',
        ),
        migrations.AddField(
            model_name='fiere',
            name='cropping_hover',
            field=image_cropping.fields.ImageRatioField('image_hover', '500x281', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='500x281 hover'),
        ),
        migrations.AddField(
            model_name='fiere',
            name='image_hover',
            field=models.ImageField(blank=True, null=True, upload_to='fiere', verbose_name='Logo Hover'),
        ),
        migrations.AlterField(
            model_name='fiere',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='fiere', verbose_name='Logo Neutro'),
        ),
    ]
