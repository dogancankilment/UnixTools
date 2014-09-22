from django import forms


class CommandForm(forms.Form):
    entry = forms.CharField(max_length=100)