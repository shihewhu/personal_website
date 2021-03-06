# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160108_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('job_company', models.CharField(db_index=True, max_length=100, unique=True)),
                ('self_introduction', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='background_picture',
            field=models.ImageField(default=b'blog/static/img/post-bg.img', upload_to=b'blog/static/img/'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
