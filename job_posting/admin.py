from django.contrib import admin

from .models import Job_Details
# Register your models here.
class JobDetailsAdmin(admin.ModelAdmin):
	list_display = ['company','company_website','industry','job_title','description','job_posting','role','location','job_type','remote','skills_required','timestamp','updated']
	class Meta :
		model = Job_Details
admin.site.register(Job_Details,JobDetailsAdmin)