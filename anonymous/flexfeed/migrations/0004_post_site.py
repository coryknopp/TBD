# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexfeed', '0003_post_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='site',
            field=models.CharField(default='', help_text='The social media site this post was made on.', max_length=50),
            preserve_default=False,
        ),
    ]