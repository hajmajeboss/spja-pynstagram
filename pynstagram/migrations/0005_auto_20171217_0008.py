# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 23:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pynstagram', '0004_auto_20171216_2217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['name']},
        ),
    ]
