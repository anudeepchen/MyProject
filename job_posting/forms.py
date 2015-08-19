from django import forms
from .models import Job_Details
        
class JobDetailsForm(forms.ModelForm):
    # Initiate the placeholder and id for all fields
    def __init__(self, *args, **kwargs):
            super(JobDetailsForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Job_Details
        fields = '__all__'
        