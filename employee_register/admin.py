from django.contrib import admin
from .models import Employee_Profile

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
	list_display = ['company','company_email','alternate_email','phone']
	class Meta:
		model = Employee_Profile
admin.site.register(Employee_Profile,RegisterAdmin)