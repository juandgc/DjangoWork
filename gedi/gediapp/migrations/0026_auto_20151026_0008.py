# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0025_auto_20151025_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capituloslibros',
            old_name='isbn_libro',
            new_name='ISBN_libro',
        ),
        migrations.RenameField(
            model_name='capituloslibros',
            old_name='integrante',
            new_name='autores',
        ),
    ]
