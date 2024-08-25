from typing import Any
from django import forms 
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        labels = {'name':'Enter Your Name','email':'Enter Your Email','password':'Enter Your Password'}
        help_text = {'name':'Enter Your Full Name Please'}
        error_messages = {'name':{'required':'Name Field is required. You cannot bypass it.'}}
        widgets = {'password':forms.PasswordInput,'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter Your Name'})}
  

    

   
    
   
    