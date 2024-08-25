from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django import forms 

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ['username','first_name','last_name','email']
        
