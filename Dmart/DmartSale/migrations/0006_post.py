# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-21 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DmartSale', '0005_auto_20190521_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=20)),
                ('post_author', models.CharField(max_length=100)),
                ('post_date', models.DateField()),
            ],
            options={
                'db_table': 'dmart_post',
            },
        ),
    ]
