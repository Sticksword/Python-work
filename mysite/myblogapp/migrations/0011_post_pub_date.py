# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0010_remove_post_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default='2002-20-02 02:20:00.000000', verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
