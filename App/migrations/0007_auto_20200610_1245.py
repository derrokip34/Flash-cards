# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-10 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20200610_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcard',
            name='subject',
        ),
        migrations.AddField(
            model_name='flashcard',
            name='subject',
            field=models.ManyToManyField(to='App.Subject'),
        ),
    ]
