from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 

class SignUpForm(UserCreationForm):
    # This portion will be used UsercreationForm or Parent Form related fields 
    password2 = forms.CharField(label="Confirm Password(Again)",widget=forms.PasswordInput)
    
    class Meta:
        # This portion will be used for model related fields 
        model = User 
        fields = ['username','first_name','last_name','email']
        labels = {'email':"Email"} 