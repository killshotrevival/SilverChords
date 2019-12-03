from django import forms
from .models import work_info


class beatupload(forms.ModelForm):
    class Meta:
        model = work_info
        fields = ['beat_name', 'beat', 'genre', 'beat_img', 'beat_desc']

class searchform(forms.Form):
    search_token = forms.CharField(max_length=100, label='search_token')