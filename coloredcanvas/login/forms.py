from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from login.models import Painter

class UserForm(UserCreationForm):
	class Meta():
		model=User
		fields=['username','email','password','first_name','last_name']

class RegisterForm(forms.ModelForm):
	class Meta():
		model=Painter
		fields=['Adress','Nationality','Phone','Registration_type']
