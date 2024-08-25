from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField(label="Your Name",label_suffix=" ",initial="Ali etc")
    email = forms.EmailField(label="Your Email Address",required=False,disabled=True,help_text="Just to debug the code ")
    phone_number = forms.IntegerField(label="Your Contact Number")
    key = forms.CharField(widget=forms.HiddenInput())