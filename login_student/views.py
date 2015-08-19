from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import login,logout as custom_logout
from django.core.context_processors import csrf
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password,check_password
#from .models import FailedLogin
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from datetime import datetime,timezone,timedelta
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.utils.timezone import utc,make_aware
import pytz
import datetime
#from register.models import Register
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
# Login page
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('student_login.html',c)

def auth_view(request):
    email = request.POST.get('email','')
    username = email + 'student'
    password = request.POST.get('password','')
    page = "login.html"
    user = auth.authenticate(username = username, password = password)
    if user is not None :
        auth.login(request,user)
        return HttpResponseRedirect('accounts/job_details/')
    else :
        messages.error(request, "Username/Password doesn't match. Please try again!")
        return render_to_response(page, locals(), context_instance=RequestContext(request))

def logout(request):
    custom_logout(request)
    return render_to_response('logout.html')

# Method is invoked when user clicks 'Forgot Password'
def forgot_password(request):
    context = {}
    context.update(csrf(request))
    template = "forgot_password.html"
    return render_to_response(template, context) 
        
#Customer Page
@login_required
def customer_page(request):
    user = request.user
    context = {"first_name" : user.first_name,"last_name" : user.last_name}
    context.update(csrf(request))
    template = "customer_page.html"
    return render_to_response(template,context,context_instance = RequestContext(request,locals()))
   

def enter_email(request):
    if request.method == 'POST':        
        email = request.POST.get('email','')
        user = User.objects.get(email = email)
        if user is not None:
            context ={
                        'email': user.email,
                        'domain': '127.0.0.1:8000', #or your domain
                        'site_name': 'example',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),                      
                        'protocol': 'http',}
            rendered = loader.render_to_string('password_reset_email.html',context)
            send_mail('change password', rendered,'contact.skycision@gmail.com', [user.email],fail_silently=False)
            return HttpResponseRedirect('/accounts/login')
        else : return HttpResponseRedirect('/accounts/invalid')
    else:
        return HttpResponseRedirect('/accounts/invalid')

# Verifies 'uidb64' and 'token' are valid 
def new_password(request,uidb64,token):
    assert uidb64 is not None and token is not None  # checked by URLconf
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(id = uid)
    except (TypeError, ValueError, OverflowError, Register.DoesNotExist):
        user = None   
    if user is not None and default_token_generator.check_token(user, token):
        context = {}
        context.update(csrf(request))
        template = "new_password.html"
        return render_to_response(template, context)
    
    
# Method allows user to the change the password    
def set_password(request):
    print(request.method)
    if request.method == 'POST':
        password1 = request.POST.get('newpassword','')
        password2 = request.POST.get('confirmpassword','')
        email = request.POST.get('email','')
        if password1 == password2 :
            password = make_password(password1,salt = None,hasher = 'bcrypt_sha256')
            user = User.objects.get(email = email)
            if user is not None :
                user.password = password
                user.save()
                return HttpResponseRedirect('/accounts/login')
            else : return HttpResponseRedirect('/accounts/invalid')
        else : return HttpResponseRedirect('/accounts/invalid')
    else : return HttpResponseRedirect('/accounts/invalid')
    
    
    
