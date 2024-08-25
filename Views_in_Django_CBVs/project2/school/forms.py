from django import forms 

class ContactUs(forms.Form):
    name = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=70)

