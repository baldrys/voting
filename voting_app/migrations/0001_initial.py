# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-23 19:43
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
                ('image', models.ImageField(upload_to='img')),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Персонаж',
                'verbose_name_plural': 'Персонажи',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('votes_to_win', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Голосование',
                'verbose_name_plural': 'Голосования',
            },
        ),
        migrations.CreateModel(
            name='Vote_for_character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes_number', models.IntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting_app.Character')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting_app.Vote')),
            ],
            options={
                'verbose_name': 'Голосование за персонажа',
                'verbose_name_plural': 'Голосования за персонажей',
            },
        ),
        migrations.AddField(
            model_name='character',
            name='vote',
            field=models.ManyToManyField(through='voting_app.Vote_for_character', to='voting_app.Vote'),
        ),
        migrations.AlterUniqueTogether(
            name='vote_for_character',
            unique_together=set([('vote', 'character')]),
        ),
    ]
