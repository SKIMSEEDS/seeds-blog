# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-01 15:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoty',
            new_name='Category',
        ),
    ]