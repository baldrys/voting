# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-22 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0002_auto_20180922_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='vote',
            field=models.ManyToManyField(through='voting_app.VoteForCharacter', to='voting_app.Vote'),
        ),
    ]