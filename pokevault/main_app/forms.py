from django.forms import ModelForm, DateInput
from .models import Condition

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