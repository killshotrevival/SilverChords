from django import forms
from .models import work_info, reviews


class beatupload(forms.ModelForm):
    class Meta:
        model = work_info
        fields = ['beat_name', 'beat', 'genre', 'beat_img', 'beat_desc', 'price']

class searchform(forms.Form):
    search_token = forms.CharField(max_length=100, label='search_token')

class reviewsform(forms.ModelForm):
    class Meta:
        model = reviews
        fields = ['rating', 'comment']