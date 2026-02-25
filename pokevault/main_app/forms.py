from django.forms import ModelForm, DateInput, URLInput
from .models import Condition, Card

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'set_name', 'rarity', 'description', 'image_url']
        widgets = {
            'image_url': URLInput(attrs={
            'placeholder': 'Find cards at pokemoncard.io/card-database'})
        }

class ConditionForm(ModelForm):
    class Meta:
        model = Condition
        fields = ['date', 'grade']
        widgets = {
            'date': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select A Date',
                    'type': 'date'
                }
            )
        }