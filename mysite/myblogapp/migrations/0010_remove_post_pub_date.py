# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0009_auto_20141116_0420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
    ]
