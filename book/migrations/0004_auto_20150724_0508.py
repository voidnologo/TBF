# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20150722_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='sub_title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='publish_date',
            field=models.DateField(null=True, verbose_name=b'date published'),
        ),
    ]
