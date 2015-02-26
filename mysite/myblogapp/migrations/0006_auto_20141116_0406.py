# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0005_auto_20141116_0350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='question_text',
            new_name='post_text',
        ),
    ]
