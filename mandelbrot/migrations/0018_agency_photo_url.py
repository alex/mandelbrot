# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0017_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='photo_url',
            field=models.URLField(blank=True),
        ),
    ]
