__author__ = 'Michael'

from django import forms


class BulletinForm(forms.Form):
    title = forms.CharField(label='Bulletin Title:', max_length=100)
    location = forms.CharField(label='Location:', max_length=100)
    author = forms.CharField(label='Author:', max_length=100)
    body = forms.CharField(label='Description:', widget=forms.Textarea)
