# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-05-10 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20200510_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
        migrations.AlterField(
            model_name='mainwheel',
            name='img',
            field=models.CharField(max_length=300),
        ),
    ]
