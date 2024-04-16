from django import forms
from .models import Food

class InputNameForm(forms.ModelForm):
  class Mete:
    model = Food