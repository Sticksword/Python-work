# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0007_auto_20141116_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_text',
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
