from django.contrib import admin
from .models import Student_Profile

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
	list_display = ['email','phone']
	class Meta:
		model = Student_Profile
admin.site.register(Student_Profile,RegisterAdmin)