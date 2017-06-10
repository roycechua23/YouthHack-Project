# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-10 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='user_organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=100, unique=True)),
                ('representative', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginApp.user_account')),
            ],
        ),
        migrations.CreateModel(
            name='user_speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('age', models.IntegerField(verbose_name=3)),
                ('job_title', models.CharField(max_length=45)),
                ('contact_number', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginApp.user_account')),
            ],
        ),
    ]
