# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='fecha_fin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='pic',
            field=models.ImageField(upload_to='news/'),
        ),
    ]
