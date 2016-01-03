"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'myproject.views.home'),
    url(r'^howitworks/$', 'myproject.views.howitworks'),
    url(r'^admin/', include(admin.site.urls)),
    
    #Student Register
    url(r'^accounts/student_register/$', 'student_register.views.register'),
    url(r'^accounts/register_user/$', 'student_register.views.register_user'),
    
    #Employee Register
    url(r'^accounts/referral_register/$', 'employee_register.views.employee_register'),
    url(r'^accounts/register_referral/$', 'employee_register.views.employee_register_user'),

    #Job Posting
    url(r'^accounts/job/$', 'job_posting.views.job'),
    url(r'^accounts/job_posting/$', 'job_posting.views.job_posting'),
    
    #Student Login
     url(r'^accounts/student_login/$', 'login_student.views.login'),
     
    #Employee Login
     url(r'^accounts/employee_login/$', 'login_employee.views.login'),
     
    #Job_details
    url(r'^accounts/job_details/$', 'job_posting.views.fetch_jobs'),

    #Linkedin
    url(r'^auth/linkedin/$', 'myproject.views.loginsuccess'),
    url(r'^auth/login/$', 'myproject.views.login'),
    url(r'^auth/manage/$', 'myproject.views.Manage'),
    
    #glassdoor
     url(r'^auth/glassdooor/$', 'myproject.views.get_glassdoor'),
     
     
     #buzzsumo
     
      url(r'^auth/buzzsumo/$', 'myproject.views.customerlist'),
      url(r'^auth/klout/$', 'myproject.views.kloutApi'),
     #test
     url(r'^auth/test/$', 'myproject.views.test'),
]



# Static files pattern
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)