from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Employee_Profile(models.Model):
    company = models.CharField(max_length=120, null=False, blank=False, default="")
    company_email = models.EmailField(null=False, blank=False, default="", unique = True)
    alternate_email =  models.EmailField(null=False, blank=False, default="", unique = True)
    phone_regex = RegexValidator(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
    phone = models.CharField(max_length=15, validators=[phone_regex], null = False, blank=False, default="")
    
    
    def _str_(self):
        return self.email
