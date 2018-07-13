from django import forms
from .models import CanGet, CanDo


class DishForm(forms.ModelForm):
    """form of ingredient that can be get"""
    name = forms.CharField(max_length=10)
    class Meta:
        model = CanDo
        fields = ['name', 'type']
        labels = {
            'name': '菜名'
        }


class IngredientForm(forms.ModelForm):
    """form of ingredient that can be get"""
    name = forms.CharField(max_length=10)
    cal = forms.NumberInput()
    class Meta:
        model = CanGet
        fields = ['name', 'cal']

        labels = {
            'name': '食材'
        }
