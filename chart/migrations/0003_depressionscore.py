# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0002_delete_monthlyweatherbycity'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepressionScore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('depression_score_week1', models.IntegerField(default=0)),
                ('depression_score_week2', models.IntegerField(default=0)),
                ('depression_score_week3', models.IntegerField(default=0)),
                ('depression_score_week4', models.IntegerField(default=0)),
                ('depression_score_week5', models.IntegerField(default=0)),
                ('depression_score_week6', models.IntegerField(default=0)),
                ('depression_score_week7', models.IntegerField(default=0)),
                ('depression_score_week8', models.IntegerField(default=0)),
            ],
        ),
    ]
