from django import forms
from .models import CreateBook

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = CreateBook
        fields = ['title', 'author', 'quantity', 'price']
