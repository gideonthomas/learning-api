# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competencies', '0002_competency'),
        ('skills', '0002_skill'),
        ('weblitskills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebLitSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('competencies', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='weblitskills', to='competencies.Competency')),
                ('skills', models.ManyToManyField(blank=True, related_name='weblitskills', to='skills.Skill')),
            ],
        ),
    ]
