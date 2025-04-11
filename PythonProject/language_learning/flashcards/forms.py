from django import forms
from .models import Flashcard


class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['word', 'translation', 'example_usage']
        widgets = {
            'example_usage': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        word = cleaned_data.get('word')
        translation = cleaned_data.get('translation')

        if word and translation and word.lower() == translation.lower():
            raise forms.ValidationError("Слово и перевод не должны быть одинаковыми")

        return cleaned_data
