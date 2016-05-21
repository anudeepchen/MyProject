from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class Student_Profile(models.Model):    
    user  = models.OneToOneField(User,primary_key=True)
    email = models.EmailField(null=False, blank=False, default="", unique = True)
    #phone_regex = RegexValidator(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
    #phone = models.CharField(max_length=15, validators=[phone_regex], null = False, blank=False, default="")
    location=models.CharField(max_length=120,null=False,default="")
    def _str_(self):
        return self.email
