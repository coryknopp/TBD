# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 21:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flexfeed', '0011_auto_20171121_1510'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='Media_Group',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='groups',
            new_name='media_group',
        ),
    ]