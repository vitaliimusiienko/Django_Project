from .models import Notes
from django.forms import ModelForm, TextInput, Textarea

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']
        
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title'}),
                
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'text'})
        }