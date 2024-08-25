from typing import Any
from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # cleaning whole form using built-in method 
    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        valpassword = self.cleaned_data['password']
        if len(valname) < 4:
            raise forms.ValidationError("SHort Name ")
        else:
            return {'name':valname}
   
    