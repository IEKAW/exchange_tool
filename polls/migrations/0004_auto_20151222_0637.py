# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_kessai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kessai',
            name='kendama_num',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
