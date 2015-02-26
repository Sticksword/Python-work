# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20141203_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='author',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='blog_id',
            field=models.AutoField(unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='location',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='title',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
