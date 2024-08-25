from django import forms 
from .models import User 
from django.core import validators 

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User 
        fields = '__all__'

        