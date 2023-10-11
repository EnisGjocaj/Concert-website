from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from . models import RegisterModel

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username', 
        'class': 'w-full py-2 px-4 rounded-xl text-black'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password', 
        'class': 'w-full py-2 px-4 rounded-xl text-black'   
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder':'Your username', 
        'class': 'w-full py-2 px-4 rounded-xl text-black'
	}))

    email = forms.CharField(widget=forms.EmailInput(attrs={
		'placeholder':'Your email', 
		'class': 'w-full py-2 px-4 rounded-xl text-black'
	}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password', 
        'class': 'w-full py-2 px-4 rounded-xl text-black'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat your password', 
        'class': 'w-full py-2 px-4 rounded-xl text-black'
    }))

class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterModel
        fields = ('name', 'surname', 'email', 'number', 'status')

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'w-full text-black py-2 px-4 rounded-xl'
    }), label=False)

    surname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Mbiemer',
        'class': 'w-full text-black py-2 px-4 rounded-xl'
    }), label=False)

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'w-full text-black py-2 px-4 rounded-xl'
    }), label=False)

    number = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder': 'Num',
        'class': 'w-full text-black py-2 px-4 rounded-xl'
    }), label=False)
