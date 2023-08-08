from django import forms
from .models import CreateBook

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = CreateBook
        fields = ['title', 'author', 'publication_date', 'quantity', 'price']
