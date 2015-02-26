# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('blog_id', models.AutoField(default=0, serialize=False, primary_key=True)),
                ('title', models.CharField(default=b'', unique=True, max_length=100)),
                ('location', models.CharField(default=b'', unique=True, max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('author', models.CharField(default=b'', unique=True, max_length=100)),
                ('body', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
