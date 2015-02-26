# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0006_auto_20141116_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=b'2002-02-20 06:00', verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
