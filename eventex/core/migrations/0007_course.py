# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160212_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='título')),
                ('start', models.TimeField(blank=True, null=True, verbose_name='início')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
                ('slots', models.IntegerField()),
                ('speakers', models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='palestrante')),
            ],
            options={
                'verbose_name_plural': 'palestras',
                'verbose_name': 'palestra',
                'abstract': False,
            },
        ),
    ]
