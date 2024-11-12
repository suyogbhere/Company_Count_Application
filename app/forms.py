from allauth.account.forms import LoginForm, SignupForm
from django import forms
from app .models import File, Company_data 


class Fileform(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']
        widgets= {'file': forms.FileInput(attrs={'class':'form-control'})}



