# forms.py
from django import forms

class YAMLForm(forms.Form):
    yaml_data = forms.CharField(widget=forms.Textarea)
