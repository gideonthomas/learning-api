# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblitskills', '0003_auto_20160818_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblitskill',
            name='text',
        ),
        migrations.AddField(
            model_name='weblitskill',
            name='name',
            field=models.CharField(default=123, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weblitskill',
            name='short_name',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
    ]
