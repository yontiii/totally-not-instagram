# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-19 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('image_name', models.CharField(max_length=20)),
                ('image_caption', models.TextField(max_length=150)),
                ('likes', models.IntegerField()),
                ('comments', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(upload_to='profiles/')),
                ('bio', models.TextField(max_length=500)),
                ('website', models.CharField(blank=True, max_length=10)),
                ('phone_number', models.CharField(max_length=10)),
                ('followers', models.ManyToManyField(blank=True, related_name='followers_profile', to='insta.Profile')),
                ('following', models.ManyToManyField(blank=True, related_name='following_profile', to='insta.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta.Profile'),
        ),
    ]
