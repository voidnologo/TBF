# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20150814_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='sub_title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
