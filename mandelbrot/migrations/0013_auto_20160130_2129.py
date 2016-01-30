# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0012_agency'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'verbose_name': 'agency', 'verbose_name_plural': 'agencies'},
        ),
        migrations.AddField(
            model_name='project',
            name='agencies',
            field=models.ManyToManyField(related_name='projects', to='mandelbrot.Agency'),
        ),
    ]