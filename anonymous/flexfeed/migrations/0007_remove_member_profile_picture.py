# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flexfeed', '0006_auto_20171027_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='profile_picture',
        ),
    ]