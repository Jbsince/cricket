from django import forms
from . models import profile

class playerForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['name','country','dob','role','img']