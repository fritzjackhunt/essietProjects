from django import forms
from django.core.exceptions import ValidationError
from django.forms.forms import Form
from django.forms import ModelForm

from .models import Newsletter

class NewsletterForm(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Newsletter
        fields = ('email',)

