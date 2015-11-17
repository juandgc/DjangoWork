# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0024_remove_capituloslibros_certificado_entidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capituloslibros',
            old_name='ISBN_libro',
            new_name='isbn_libro',
        ),
    ]
