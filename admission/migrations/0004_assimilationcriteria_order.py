# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-29 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0003_assimilationcriteria'),
    ]

    operations = [
        migrations.AddField(
            model_name='assimilationcriteria',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
