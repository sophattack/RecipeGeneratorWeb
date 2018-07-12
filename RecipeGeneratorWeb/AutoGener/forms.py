from django import forms
from .models import CanGet, CanDo


class IngredientForm(forms.ModelForm):
    """form of ingredient that can be get"""
    name = forms.CharField(max_length=10)
    cal = forms.NumberInput()
    class Meta:
        model = CanDo
        fields = ['name', 'type']
        # widgets = {
        #     'type': forms.Select(attrs={'class': 'test-type-select'})
        # }
        labels = {
            'name': '菜名'
        }
