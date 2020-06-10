# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-10 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20200610_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcard',
            name='subject',
        ),
        migrations.AddField(
            model_name='flashcard',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.Subject'),
        ),
    ]