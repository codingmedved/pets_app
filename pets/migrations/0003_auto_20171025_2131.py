# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-25 18:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20171025_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='type',
            new_name='animal_kind',
        ),
    ]
