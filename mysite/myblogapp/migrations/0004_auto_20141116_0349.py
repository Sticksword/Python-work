# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0003_auto_20141116_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'], verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
