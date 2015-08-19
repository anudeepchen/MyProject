# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('student_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.EmailField(max_length=254, default='', unique=True)),
                ('phone', models.CharField(validators=[django.core.validators.RegexValidator(regex='^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]?\\d{3}[\\s.-]?\\d{4}$')], max_length=15, default='')),
            ],
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
