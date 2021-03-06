# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import routes.models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0005_auto_20170311_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directions', routes.models.JSONFieldCustom()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routes.Route')),
            ],
        ),
    ]
