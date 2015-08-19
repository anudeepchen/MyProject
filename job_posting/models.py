from django.db import models
from django.core.validators import RegexValidator,URLValidator
# Create your models here.

class Job_Details(models.Model):
    company = models.CharField(max_length=120, null=False, blank=False, default="")
    url_regex = URLValidator
    company_website = models.CharField(max_length=30, validators=[url_regex], null = False, blank=False, default="")
    industry = models.CharField(max_length=120, null=False, blank=False, default="")
    job_title = models.CharField(max_length=120, null=False, blank=False, default="")
    description = models.TextField(max_length=250, null=False, blank=False, default="")
    job_posting = models.CharField(max_length=120, null=False, blank=False, default="")
    role = models.CharField(max_length=120, null=False, blank=False, default="")
    location = models.CharField(max_length=120, null=False, blank=False, default="")
    
    FULL_TIME = 'FT'
    CONTRACTOR = 'CO'
    INTERN = 'IN'
    INTEREST_CHOICES = (
        (FULL_TIME, 'Full-time'),
        (CONTRACTOR, 'Contractor'),
        (INTERN, 'Intern'),
    )
    job_type = models.CharField(max_length=2, choices=INTEREST_CHOICES, default="")
    remote = models.CharField(max_length=120, null=False, blank=False, default="")
    skills_required = models.CharField(max_length=120, null=False, blank=False, default="")
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    