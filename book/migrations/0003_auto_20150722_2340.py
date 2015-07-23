# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20150722_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='file_path',
            field=models.CharField(max_length=200),
        ),
    ]
