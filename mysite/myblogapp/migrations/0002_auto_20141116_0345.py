# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=b'DEFAULT DATE', verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='question_text',
            field=models.CharField(default=b'DEFAULT TEXT', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default=b'DEFAULT TAG', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=b'DEFAULT TITLE', max_length=500),
            preserve_default=True,
        ),
    ]
