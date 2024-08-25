from .models import Student
from django import forms 

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {'name':forms.TextInput(attrs={'class':"form-control my-4",'placeholder':'Enter Your Name'}),
                   'email':forms.EmailInput(attrs={'class':"form-control my-4",'placeholder':"Enter Your Email"}),
                   'password':forms.PasswordInput(render_value=True,attrs={'class':"form-control my-4",'placeholder':"Enter Your Password"})}
        
        labels = {
            'name':"Name",
            'email':"Email",
            'password':"Password"
        }
