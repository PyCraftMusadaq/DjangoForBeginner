from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ['username','first_name','last_name','email']



class ChangePassword(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    labels = {"password1":"Enter Old Password","password2":"Enter New Password"}