# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Details',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('company', models.CharField(max_length=120, default='')),
                ('company_website', models.CharField(validators=[django.core.validators.URLValidator], max_length=30, default='')),
                ('industry', models.CharField(max_length=120, default='')),
                ('job_title', models.CharField(max_length=120, default='')),
                ('description', models.TextField(max_length=250, default='')),
                ('job_posting', models.CharField(max_length=120, default='')),
                ('role', models.EmailField(max_length=254, unique=True, default='')),
                ('location', models.CharField(max_length=120, default='')),
                ('job_type', models.CharField(max_length=2, choices=[('CL', 'Full-time'), ('IN', 'Contractor'), ('PA', 'Intern')], default='')),
                ('remote', models.CharField(max_length=120, default='')),
                ('skills_required', models.CharField(max_length=120, default='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
