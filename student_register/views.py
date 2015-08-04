from django.shortcuts import render
from .forms import RegisterForm
from .models import Register
from django.core.context_processors import csrf
from django.contrib import messages
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from django.db import IntegrityError

# Create your views here.

# Method calls the register.html form allowing user to enter his personal information       
def register(request):
    context = {"form" : RegisterForm()}
    context.update(csrf(request))
    template = "student_register.html"
    return render_to_response(template, context)


# Method allows the user to enter the information and submit
def register_user(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        try :
            if form.is_valid():
                old_password = form['password'].value()
                form.cleaned_data['password'] = make_password(old_password,salt = None,hasher = 'bcrypt_sha256')     
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                password = form.cleaned_data['password']
                new_form = Register(first_name=first_name,last_name=last_name,email=email,phone=phone,password=password)
                new_form.save()
                form = RegisterForm()
                return HttpResponseRedirect('/')
            else :
                messages.error(request, "There is an error in your submission!")
        except IntegrityError:
            messages.error(request, "The email you entered is already exist!")
            form = RegisterForm()
    else : form = RegisterForm()
    #context = {"form" : RegisterForm()}
    template = "student_register.html"
    return render_to_response(template, context_instance = RequestContext(request,locals()))