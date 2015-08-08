from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Register(models.Model):
    first_name = models.CharField(max_length=120, null=False, blank=False, default="")
    last_name = models.CharField(max_length=120, null=False, blank=False, default="")
    email = models.EmailField(null=False, blank=False, default="", unique = True)
    phone_regex = RegexValidator(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
    phone = models.CharField(max_length=15, validators=[phone_regex], null = False, blank=False, default="")
    password = models.CharField(max_length=120, null=False, blank=False, default="")
    confirm_password = models.CharField(max_length=120, null=False, blank=False, default="")
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    acc_locked = models.BooleanField(default = False)
    last_login = models.DateTimeField(auto_now_add = True, auto_now = False)
    
    def _str_(self):
        return self.email


    #User.profile = property(lambda u : UserProfile.objects.get_or_create(user=u)[0])