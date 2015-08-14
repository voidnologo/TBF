# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20150724_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='middle_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
