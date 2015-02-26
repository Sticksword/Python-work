# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_bulletin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='blog_id',
            field=models.AutoField(default=0, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
