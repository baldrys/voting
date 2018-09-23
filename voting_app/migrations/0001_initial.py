# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-22 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('votes_to_win', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VoteForCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes_number', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting_app.Character')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting_app.Vote')),
            ],
        ),
    ]