from typing import Any
from django import forms 
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        labels = {'name':'Enter Your Name','email':'Enter Your Email','password':'Enter Your Password'}
        widgets = {'password':forms.PasswordInput}
  

    

   
    
   
    