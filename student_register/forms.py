from .models import Register
from django.contrib import messages
from django import forms
#from nocaptcha_recaptcha.fields import NoReCaptchaField

class RegisterForm(forms.ModelForm):
	
	def __init__(self,*args,**kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['phone'].widget.attrs['placeholder'] = 'Phone number'
		self.fields['password'].widget.attrs['placeholder'] = 'Password'
		self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
	
	def clean(self):
		if 'password' in self.cleaned_data and 'reenter_password' in self.cleaned_data:
			if self.cleaned_data['password'] != self.cleaned_data['reenter_password']:
				raise forms.ValidationError('Input passwords does not match')	
		return self.cleaned_data

	class Meta:
		model = Register
		widgets = {'password' : forms.PasswordInput,'reenter_password' : forms.PasswordInput}	
		fields = '__all__'
	
	#captcha = NoReCaptchaField(gtag_attrs={'data-theme':'dark'})