from django.shortcuts import render
from .forms import RegisterForm
from .models import Student_Profile
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
                email = form.cleaned_data['email']
                username = email + 'student'
                phone = form.cleaned_data['phone']
                new_user = User.objects.create_user(username,email,
                                        form.cleaned_data['password'])
                new_user.first_name = form.cleaned_data['first_name']
                new_user.last_name = form.cleaned_data['last_name']
                new_user.save()
                
                new_form = Student_Profile(email=email,phone=phone)
                new_form.save()
                
                form = RegisterForm()
                return HttpResponseRedirect('/')
            else :
                messages.error(request, "There is an error in your submission!")
        except IntegrityError:
            messages.error(request, "The email you entered is already exists!")
            form = RegisterForm()
    else : form = RegisterForm()
    template = "student_register.html"
    print(messages)
    return render_to_response(template, context_instance = RequestContext(request,locals()))


