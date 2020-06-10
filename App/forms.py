from django import forms
from .models import FlashCard

class PostFlashCard(forms.ModelForm):
    class Meta:
        model = FlashCard
        exclude = ['user']
        widgets = {
            'card_notes':forms.Textarea(),
            'subject': forms.CheckboxSelectMultiple()
        }