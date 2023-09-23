from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from .models import *



class userLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        label_suffix='',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Enter Your Username'})
    )
    
    password = forms.CharField(
        label='Password',
        label_suffix='',
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter Your Password'})
    )
    class Meta:
        model = User
        fields=['username']

class UserSignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        label_suffix='',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Enter Your Username'})
    )
    
    email = forms.EmailField(
        label='Email',
        label_suffix='',
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'xxxxx@gmail.com'})
    )
    
    first_name = forms.CharField(
        label='First Name',
        label_suffix='',
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your first Name'})
    )
    
    last_name = forms.CharField(
        label='Last Name',
        label_suffix='',
        widget=forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Enter Your Last Name'})
    )

    password1 = forms.CharField(
        label='Password',
        label_suffix='',
        widget=forms.PasswordInput(attrs={'class': 'form-control' ,'placeholder':'Enter Your password'})
    )

    password2 = forms.CharField(
        label='Confirm Password',
        label_suffix='',
        widget=forms.PasswordInput(attrs={'class': 'form-control' ,'placeholder':'Please confirm Your Password'})
    )
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']


class DateInput(forms.DateInput):
    input_type = 'date'

GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
)

class UserProfileForm(forms.ModelForm):

    contact = forms.CharField(
        label='Contact',
        label_suffix='',
        max_length=11,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'+91-xxxxxxx'})
    )

    gender = forms.ChoiceField(
        label='Gender',
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Please Select Your Gender'})
    )


    date_of_birth = forms.DateField(
        label='Date of Birth',
        label_suffix='',
        widget=DateInput(attrs={'class': 'form-control'}),
        input_formats=['%Y-%m-%d'],  # Define your desired date input format(s)
    )

    profile_pic = forms.ImageField(
        label='Profile Picture',
        label_suffix='',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )
    class Meta:
        model =UserProfile
        fields=['contact','gender','date_of_birth','profile_pic']
