from django import forms
from .models import CanGet, CanDo, DishType


class DishForm(forms.ModelForm):
    """form of ingredient that can be get"""
    name = forms.CharField(max_length=10)
    type = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=DishType.objects.all())
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
