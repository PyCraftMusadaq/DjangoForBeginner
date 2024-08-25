from django import forms 

class UserRegistration(forms.Form):
    name= forms.CharField()
    email = forms.EmailField()