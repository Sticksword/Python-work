__author__ = 'Michael'

from django import forms


class RegistrationForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)