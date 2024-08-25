from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms  
from django.utils.translation import gettext, gettext_lazy as _ 
from .models import POST

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(required=True,label="Password",max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(required=True,label="Confirm Password(again)",max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email']
        labels = {"first_name":"First Name",'last_name':"Last Name"}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'}),
                   }
    def __init__(self, *args: Any, **kwargs: Any):
        super(SignUpForm,self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required=True 


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':True,'class':"form-control"}))


class DBForm(forms.ModelForm):
    class Meta:
        model = POST 
        fields = ['title','desc']
        labels = {'title':"Title","desc":"Description"}
        widgets = {'title':forms.TextInput(attrs={'class':"form-control"}),
                   'desc':forms.Textarea(attrs={'class':"form-control"})}

