from django.shortcuts import render
from .forms import RegisterForm
from .models import Employee_Profile
from django.core.context_processors import csrf
from django.contrib import messages
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
# Create your views here.

# Method calls the register.html form allowing user to enter his personal information       
def employee_register(request):
    context = {"form" : RegisterForm()}
    context.update(csrf(request))
    template = "referral_register.html"
    return render_to_response(template, context)


# Method allows the user to enter the information and submit
def employee_register_user(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        print("dyude",form.is_valid())
        try :
            print(form.is_valid())
            if form.is_valid():
                company = form.cleaned_data['company']
                company_email = form.cleaned_data['company_email']
                alternate_email = form.cleaned_data['alternate_email']
                phone = form.cleaned_data['phone']
                new_user = User.objects.create_user(company_email,company_email,
                                        form.cleaned_data['password'])
                new_user.first_name = form.cleaned_data['first_name']
                new_user.last_name = form.cleaned_data['last_name']
                new_user.save()
                
                new_form = Employee_Profile(company=company,company_email=company_email,alternate_email=alternate_email,phone=phone)
                new_form.save()
                
                form = RegisterForm()
                return HttpResponseRedirect('/accounts/employee_login')
            else :
                messages.error(request, "There is an error in your submission!")
        except IntegrityError:
            messages.error(request, "The email you entered is already exists!")
            form = RegisterForm()
    else : form = RegisterForm()
    template = "referral_register.html"
    return render_to_response(template, context_instance = RequestContext(request,locals()))