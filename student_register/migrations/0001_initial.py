# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=120, default='')),
                ('last_name', models.CharField(max_length=120, default='')),
                ('email', models.EmailField(default='', unique=True, max_length=254)),
                ('phone', models.CharField(default='', validators=[django.core.validators.RegexValidator(regex='^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]?\\d{3}[\\s.-]?\\d{4}$')], max_length=15)),
                ('password', models.CharField(max_length=120, default='')),
                ('confirm_password', models.CharField(max_length=120, default='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('acc_locked', models.BooleanField(default=False)),
            ],
        ),
    ]
