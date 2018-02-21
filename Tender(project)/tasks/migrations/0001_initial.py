# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-09 17:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0002_auto_20180209_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=200)),
                ('task_text', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='events.Event')),
            ],
        ),
    ]
