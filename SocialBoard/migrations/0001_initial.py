# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-29 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=120)),
                ('post_publish_date', models.DateTimeField(verbose_name='Published date')),
                ('post_content', models.CharField(max_length=500)),
                ('post_author', models.CharField(max_length=24)),
            ],
        ),
    ]
