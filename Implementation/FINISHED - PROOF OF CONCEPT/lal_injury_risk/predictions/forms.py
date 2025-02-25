from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'position', 'height', 'weight', 'age', 'avg_minutes', 'avg_field_goals', 'injuries_last_3_years', 'total_injuries']
