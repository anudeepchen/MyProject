from .models import Register
from django.contrib import messages
from django import forms

#from nocaptcha_recaptcha.fields import NoReCaptchaField

class RegisterForm(forms.ModelForm):
	
	def __init__(self,*args,**kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		
	
	def clean(self):
		if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
			if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
				raise forms.ValidationError('Input passwords does not match')	
		return self.cleaned_data

	class Meta:
		model = Register
		widgets = {'password' : forms.PasswordInput,'confirm_password' : forms.PasswordInput}	
		fields = '__all__'
	
	#captcha = NoReCaptchaField(gtag_attrs={'data-theme':'dark'})