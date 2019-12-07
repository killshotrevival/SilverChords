from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

class registerform(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'password2']


class InfoUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['artist_photo', 'cover_photo', 'place', 'desc', 'fb', 'insta']

class NotifyForm(forms.Form):
    data = forms.CharField(max_length=200, label='data')
    header = forms.CharField(max_length=200, label='header')

