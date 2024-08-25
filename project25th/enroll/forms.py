from typing import Any
from django import forms 
from django.core import validators

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data['password']
        rpassword = self.cleaned_data['rpassword']
        if password!=rpassword:
            raise forms.ValidationError("Password Does not match")

    

   
    
   
    