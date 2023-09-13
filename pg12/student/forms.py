from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    name=forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','id':'styam'})
    )
    email= forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control'})
    )
    contact =forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class':'form-control'}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    gender = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=Student
        fields=['name','email','contact','age','gender']
        


# class StudentForm(forms.Form):
#     name=forms.CharField(
#         max_length=50,
#         widget=forms.TextInput(attrs={'class':'form-control','id':'styam'})
#     )
#     email= forms.EmailField(
#         widget=forms.EmailInput(attrs={'class':'form-control'})
#     )
#     contact =forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class':'form-control'}))
#     age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
#     gender = forms.CharField(max_length=6,widget=forms.TextInput(attrs={'class':'form-control'}))


# form ---> student