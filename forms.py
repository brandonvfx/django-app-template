from django import forms

from .models import *

__all__ = []

class SomeModelForm(forms.ModelForm):
    class Meta:
        model = SomeModel
