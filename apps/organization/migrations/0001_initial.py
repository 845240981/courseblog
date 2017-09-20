# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u5b57')),
                ('des', models.CharField(max_length=300, verbose_name='\u63cf\u8ff0')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u57ce\u5e02',
                'verbose_name_plural': '\u57ce\u5e02',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Courseorg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u673a\u6784\u540d\u79f0')),
                ('dec', models.TextField(verbose_name='\u673a\u6784\u7b80\u4ecb')),
                ('click_nums', models.ImageField(default=0, upload_to=b'', verbose_name='\u70b9\u51fb\u6570\u91cf')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u6570')),
                ('image', models.ImageField(upload_to=b'org/%Y/%m', verbose_name='\u5c01\u9762\u56fe')),
                ('address', models.CharField(max_length=150, verbose_name='\u673a\u6784\u5730\u5740')),
                ('city', models.ForeignKey(verbose_name='\u6240\u5728\u57ce\u5e02', to='organization.Citys')),
            ],
            options={
                'verbose_name': '\u6388\u8bfe\u673a\u6784',
                'verbose_name_plural': '\u6388\u8bfe\u673a\u6784',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u6559\u5e08\u540d')),
                ('click_nums', models.ImageField(default=0, upload_to=b'', verbose_name='\u70b9\u51fb\u6570\u91cf')),
                ('work_years', models.IntegerField(default=0, verbose_name='\u5de5\u4f5c\u5e74\u9650')),
                ('image', models.ImageField(upload_to=b'org/%Y/%m', verbose_name='\u6559\u5e08\u56fe\u7247')),
                ('work_company', models.CharField(max_length=150, verbose_name='\u673a\u6784\u5730\u5740')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u6570')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('points', models.CharField(max_length=50, verbose_name='\u6559\u5b66\u7279\u70b9')),
                ('org', models.ForeignKey(verbose_name='\u6240\u5c5e\u673a\u6784', to='organization.Courseorg')),
            ],
            options={
                'verbose_name': '\u6559\u5e08\u7b80\u4ecb',
                'verbose_name_plural': '\u6559\u5e08\u7b80\u4ecb',
            },
            bases=(models.Model,),
        ),
    ]
