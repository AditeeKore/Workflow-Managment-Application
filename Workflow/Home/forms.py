 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Registration

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = {'username','email','password1','password2'}
        
        