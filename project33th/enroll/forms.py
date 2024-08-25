from django.core import validators
from django import forms 
from .models import User 

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User 
        # for all fields by specifying their names
        #fields = ['name','email','password'] 
        # for all fields by just shortcut 
        fields = '__all__'
        #labels = {'name':"Enter Your Name",'email':"Enter Your Email",'password':"Enter Your Password"}
        widgets = {
            'password':forms.PasswordInput()
        }
        # This technique is used when we have to exlude one or more fields from many fields 
        #exclude = ['name']