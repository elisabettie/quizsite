# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20150807_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('wikilink', models.CharField(max_length=100)),
                ('imgsrc', models.CharField(max_length=100)),
                ('birth', models.PositiveIntegerField()),
                ('death', models.PositiveIntegerField()),
            ],
        ),
    ]
