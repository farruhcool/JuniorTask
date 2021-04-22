from django import forms

from cities.models import City
from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Train', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter name of train'
    }))

    travel_time = forms.IntegerField(label='Time of travel', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Time of travel'
    }))

    from_city = forms.ModelChoiceField(label='From city', queryset=City.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))
    to_city = forms.ModelChoiceField(label='To city', queryset=City.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Train
        fields = '__all__'
