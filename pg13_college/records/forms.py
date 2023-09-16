from django import forms 
from .models import *



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields=['name','email','age','gender']



class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=['name','email','subject','experience']