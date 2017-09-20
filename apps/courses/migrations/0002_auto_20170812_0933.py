# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='click_nums',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='course',
            name='learn_nums',
            field=models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u4eba\u6570'),
        ),
    ]
