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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=120, default='')),
                ('last_name', models.CharField(max_length=120, default='')),
                ('company', models.CharField(max_length=120, default='')),
                ('company_email', models.EmailField(max_length=254, default='', unique=True)),
                ('alternate_email', models.EmailField(max_length=254, default='', unique=True)),
                ('phone', models.CharField(max_length=15, default='', validators=[django.core.validators.RegexValidator(regex='^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]?\\d{3}[\\s.-]?\\d{4}$')])),
                ('password', models.CharField(max_length=120, default='')),
                ('confirm_password', models.CharField(max_length=120, default='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('acc_locked', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
