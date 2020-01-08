from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile, verification, advice
from beats.models import work_info

class registerform(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'password2']


class InfoUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['artist_photo', 'cover_photo', 'place', 'desc', 'fb', 'insta', 'youtube']

class BeatUpdateForm(forms.ModelForm):
    class Meta:
        model = work_info
        fields = ['beat_name', 'genre', 'beat_desc', 'price']

class NotifyForm(forms.Form):
    data = forms.CharField(max_length=200, label='data')
    hae = forms.CharField(max_length=200, label='hae')

class helpform(forms.Form):
    name = forms.CharField(max_length=100, label='name')
    email = forms.EmailField(label='email')
    message = forms.CharField(max_length=500, label='message')

class verifiform(forms.ModelForm):
    class Meta:
        model = verification
        fields = ['phone', 'email', 'vtype', 'vno', 'front_photo', 'back_photo']

class adviceform(forms.ModelForm):
    class Meta:
        model = advice
        fields = ['platform', 'content']

