from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class RegisterUserForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'email'      : forms.TextInput(attrs= {'class' : 'form-control'}),
            'first_name' : forms.TextInput(attrs = {'class':'form-control'}),
            'last_name'  : forms.TextInput(attrs = {'class':'form-control'}),    
            # 'password1' : forms.PasswordInput(attrs = {'class':'form-control', 'type':'password'}),
            # 'password2' : forms.PasswordInput(attrs = {'class':'form-control', 'type':'password'}),
        }

        labels ={
            'email': 'Email'
        }
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields =['first_name', 'last_name', 'phone' ]
        widgets ={
            'first_name' : forms.TextInput(attrs = {'class':'form-control'}),
            'last_name' : forms.TextInput(attrs = {'class':'form-control'}),
            'phone' : forms.NumberInput(attrs={'class':'form-control' , 'placeholder':'Phone'}),
        }        