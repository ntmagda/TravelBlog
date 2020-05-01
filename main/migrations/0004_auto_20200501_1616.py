# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-05-01 14:16
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_aboutus_aboutusimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='leon_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='leon_image'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='magda_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='magda_image'),
        ),
        migrations.AlterField(
            model_name='aboutusimage',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]