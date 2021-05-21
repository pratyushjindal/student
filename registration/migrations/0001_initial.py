# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FullName', models.CharField(max_length=200)),
                ('PhoneNo', models.IntegerField(default=0)),
                ('AdmissionNo', models.IntegerField(default=0)),
                ('Standard', models.IntegerField(default=0)),
                ('Section', models.CharField(max_length=200)),
            ],
        ),
    ]
