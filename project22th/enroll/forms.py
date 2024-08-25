from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        valuename = self.cleaned_data['name']
        if len(valuename) < 4:
            raise forms.ValidationError("Enter More Than 4 character")
        return valuename 
    