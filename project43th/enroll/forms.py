from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ['username','first_name','last_name','email']


class EditUserProfileForm(UserChangeForm):
    password = None 
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        labels = {"email":"Email Address"}
