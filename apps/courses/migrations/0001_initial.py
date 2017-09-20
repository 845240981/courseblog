# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u8bfe\u7a0b\u540d')),
                ('des', models.CharField(max_length=100, verbose_name='\u8bfe\u7a0b\u7b80\u4ecb')),
                ('detail', models.TextField(verbose_name='\u8bfe\u7a0b\u8be6\u60c5')),
                ('degree', models.CharField(max_length=20, choices=[(b'cj', '\u521d\u7ea7'), (b'zj', '\u4e2d\u7ea7'), (b'gj', '\u9ad8\u7ea7')])),
                ('learn_time', models.ImageField(default=0, upload_to=b'', verbose_name='\u5b66\u4e60\u65f6\u957f')),
                ('learn_nums', models.IntegerField(default=0, max_length=100, verbose_name='\u5b66\u4e60\u4eba\u6570')),
                ('click_nums', models.IntegerField(default=0, max_length=100, verbose_name='\u70b9\u51fb\u6570\u91cf')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u4eba\u6570')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('image', models.ImageField(upload_to=b'courses/%Y/%m', verbose_name='\u5c01\u9762')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u7ae0\u8282\u540d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
