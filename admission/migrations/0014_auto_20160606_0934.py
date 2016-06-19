# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-06 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0013_auto_20160603_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='bank_account_bic',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='bank_account_iban',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='bank_account_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='culture_membership',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='deduction_children',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='scholarship',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='scholarship_organization',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='solidary_membership',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='sport_membership',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='study_grant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='study_grant_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]