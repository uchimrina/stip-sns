# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-10-02 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0019_auto_20180731_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='refer_url',
            field=models.TextField(default=None, max_length=1024, null=True),
        ),
    ]