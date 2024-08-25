from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms 

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label="Confirm Password (again)", widget=forms.PasswordInput)
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email']
        labels = {'email':"Email"}
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].required = True 
        self.fields['last_name'].required = True 
       

class UserAuthentication(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #self.fields['username'].required=True 
        #self.fields['password'].required=True 
