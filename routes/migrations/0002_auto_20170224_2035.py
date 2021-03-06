# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-24 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitute', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AddField(
            model_name='coord',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routes.Route'),
        ),
    ]
