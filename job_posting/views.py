from django.shortcuts import render
from .forms import JobDetailsForm
from .models import Job_Details
from django.core.context_processors import csrf
from django.contrib import messages
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from django.db import IntegrityError

# Create your views here.

# Method calls the register.html form allowing user to enter his personal information       
def job(request):
    context = {"form" : JobDetailsForm()}
    context.update(csrf(request))
    template = "job_posting.html"
    return render_to_response(template, context)


# Method allows the user to enter the information and submit
def job_posting(request):
    
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = JobDetailsForm(request.POST)
        # check whether it's valid:
        print(form.is_valid())
        if form.is_valid():
            # save the form to the database
            save_it = form.save(commit=False)
            save_it.save()
            # reset the form
            form = JobDetailsForm()         
            messages.success(request, "Accepted")
        else:
            messages.error(request, "Rejected")
    else:
        form = JobDetailsForm()
    
    return render_to_response("job_posting.html", locals(), context_instance=RequestContext(request))


def fetch_jobs(request):
    #if request.method == "POST":
        #data = Job_Details.objects.all()
        #print(data)
        #if data is not None:
    jobs = [1,2,3,4,5]
    return render_to_response("job_display.html",{'jobs' : jobs},context_instance=RequestContext(request))