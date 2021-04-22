from django import forms

class DataForm(forms.Form):
    lat = forms.CharField(label='lattitude', max_length=3)
    lon = forms.CharField(label='longitude', max_length=3)