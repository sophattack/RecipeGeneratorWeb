from django import forms
from .models import CanGet


class IngredientForm(forms.ModelForm):
    """form of ingredient that can be get"""
    class Meta:
        model = CanGet
        fields = ['name', 'cal']
