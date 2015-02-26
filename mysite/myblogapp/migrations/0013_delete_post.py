# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0012_auto_20141116_0443'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
