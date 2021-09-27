 
from django.db.models import fields
from Home.models import MyTask
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

# class MyTaskForm(forms.ModelForm):
# 	class Meta:
# 		model = MyTask
# 		fields = ['item', 'completed']


        
        