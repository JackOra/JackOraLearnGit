# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-05-11 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_foodtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=16)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=128)),
                ('productlongname', models.CharField(max_length=200)),
                ('isxf', models.BooleanField(default=True)),
                ('pmdesc', models.BooleanField(default=True)),
                ('specifics', models.CharField(max_length=32)),
                ('price', models.FloatField(default=0)),
                ('marketprice', models.FloatField(default=1)),
                ('categoryid', models.CharField(max_length=16)),
                ('childcid', models.CharField(max_length=32)),
                ('childcidname', models.CharField(max_length=32)),
                ('dealerid', models.CharField(max_length=16)),
                ('storenums', models.IntegerField(default=5)),
                ('productnum', models.IntegerField(default=10)),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
    ]
