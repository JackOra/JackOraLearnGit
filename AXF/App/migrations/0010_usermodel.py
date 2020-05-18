# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-05-13 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_good'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=32, unique=True)),
                ('u_password', models.CharField(max_length=256)),
                ('u_email', models.CharField(max_length=128, unique=True)),
                ('u_icon', models.ImageField(upload_to='icons')),
                ('is_delete', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
