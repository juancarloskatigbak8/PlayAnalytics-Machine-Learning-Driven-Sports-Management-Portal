from django import forms
from .models import Player, JournalEntry

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['date', 'title', 'note']
