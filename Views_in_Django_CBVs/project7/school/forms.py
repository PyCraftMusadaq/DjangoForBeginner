from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=100)
    msg = forms.CharField(widget=forms.Textarea)
    

