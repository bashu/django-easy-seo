# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import seo.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=200, verbose_name='title', blank=True)),
                ('description', models.CharField(default=b'', max_length=200, verbose_name='description', blank=True)),
                ('keywords', models.CharField(default=b'', max_length=1000, verbose_name='keywords', blank=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'SEO fields',
                'verbose_name_plural': 'SEO fields',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='seo',
            unique_together=set([('content_type', 'object_id')]),
        ),
    ]
