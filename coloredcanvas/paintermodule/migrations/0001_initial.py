# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-18 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Painter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('painting_name', models.CharField(max_length=21)),
                ('painting_type', models.CharField(max_length=10)),
                ('painting_size', models.IntegerField(default=10)),
                ('painter_name', models.CharField(max_length=10)),
                ('painting_prize', models.IntegerField(default=10)),
                ('painting_picture', models.ImageField(upload_to='media/pic/')),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
