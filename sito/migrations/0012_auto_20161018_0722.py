# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-18 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0011_auto_20160912_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100, verbose_name='Titolo')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Province',
            },
        ),
        migrations.AddField(
            model_name='casehistory',
            name='body_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Descrizione Inglese'),
        ),
        migrations.AddField(
            model_name='casehistory',
            name='sottotitolo_uk',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='casehistory',
            name='titolo_uk',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='fiere',
            name='body_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Descrizione Inglese'),
        ),
        migrations.AddField(
            model_name='fiere',
            name='sottotitolo_uk',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='fiere',
            name='titolo_uk',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='body_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Descrizione Inglese'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='titolo_uk',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='showroom',
            name='body_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Descrizione_uk'),
        ),
        migrations.AddField(
            model_name='showroom',
            name='sottotitolo_uk',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='showroom',
            name='titolo_uk',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='stand',
            name='body_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Descrizione Inglese'),
        ),
        migrations.AddField(
            model_name='stand',
            name='sottotitolo_uk',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='stand',
            name='titolo_uk',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='casehistory',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sito.Province'),
        ),
        migrations.AddField(
            model_name='fiere',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sito.Province'),
        ),
        migrations.AddField(
            model_name='showroom',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sito.Province'),
        ),
        migrations.AddField(
            model_name='stand',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sito.Province'),
        ),
    ]
