from django import forms 
from .models import Student

class ContactForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control my-2','placeholder':"Enter Your Name"}),
            'email':forms.EmailInput(attrs={'class':"form-control my-2",'placeholder':"Enter Your Email"}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control my-2','placeholder':"Enter Your Password"})
        }
        labels = {'name':"Name",'email':"Email",'password':"Password"}


