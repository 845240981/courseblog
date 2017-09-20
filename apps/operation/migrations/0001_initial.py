# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200, verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='courses.Course')),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u8bc4\u8bba',
                'verbose_name_plural': '\u8bfe\u7a0b\u8bc4\u8bba',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('phone', models.CharField(max_length=20, verbose_name='\u7535\u8bdd\u53f7\u7801')),
                ('course_name', models.CharField(max_length=20, verbose_name='\u8bfe\u7a0b\u540d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u54a8\u8be2',
                'verbose_name_plural': '\u7528\u6237\u54a8\u8be2',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='courses.Course')),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u8bfe\u7a0b',
                'verbose_name_plural': '\u7528\u6237\u8bfe\u7a0b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fav_id', models.IntegerField(default=0, verbose_name='\u6570\u636eid')),
                ('fav_type', models.IntegerField(default=1, verbose_name='\u6536\u85cf\u7c7b\u578b', choices=[(1, b'\xe8\xaf\xbe\xe7\xa8\x8b'), (2, b'\xe6\x8e\x88\xe8\xaf\xbe\xe6\x9c\xba\xe6\x9e\x84'), (3, b'\xe8\xae\xb2\xe5\xb8\x88')])),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u6536\u85cfm',
                'verbose_name_plural': '\u8bfe\u7a0b\u6536\u85cfm',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.IntegerField(default=0, verbose_name='\u7528\u6237id')),
                ('message', models.CharField(max_length=300, verbose_name='\u4fe1\u606f\u5185\u5bb9')),
                ('has_read', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xb7\xb2\xe8\xaf\xbb')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
    ]
