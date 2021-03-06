# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 08:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentsProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=254)),
                ('middle_name', models.CharField(blank=True, max_length=254)),
                ('last_name', models.CharField(blank=True, max_length=254)),
                ('occupation', models.CharField(blank=True, max_length=254)),
                ('dob', models.CharField(blank=True, max_length=254)),
                ('age', models.CharField(blank=True, max_length=254)),
                ('marriage_anniversary', models.CharField(blank=True, max_length=254)),
                ('agriculture_status', models.CharField(blank=True, max_length=254)),
                ('purpose_of_buying', models.TextField(blank=True, max_length=254)),
                ('email', models.CharField(blank=True, max_length=254)),
                ('mobile', models.CharField(blank=True, max_length=254)),
                ('alternate_mobile', models.CharField(blank=True, max_length=254)),
                ('address1', models.TextField(blank=True, max_length=254)),
                ('address2', models.TextField(blank=True, max_length=254)),
                ('pin_code', models.CharField(blank=True, max_length=254)),
                ('photo', models.ImageField(null=True, upload_to='customers')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
