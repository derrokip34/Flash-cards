from django import forms
from .models import FlashCard,Subject



class PostFlashCard(forms.ModelForm):
    class Meta:
        model = FlashCard
        exclude = ['user']
        widgets = {
            'card_notes':forms.Textarea(),
            'subject':forms.Select()
        }