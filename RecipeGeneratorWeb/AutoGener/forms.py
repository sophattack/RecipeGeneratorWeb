from django import forms
from .models import CanGet, CanDo, DishType


class DishForm(forms.ModelForm):
    """form of ingredient that can be get"""
    name = forms.CharField(max_length=10)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(DishForm, self).__init__(*args, **kwargs)
        self.fields['type'] = forms.ModelMultipleChoiceField(
                widget=forms.CheckboxSelectMultiple, queryset=DishType.objects.filter(userid=self.user.id))

    class Meta:
        model = CanDo
        fields = ['name', 'type']
    #     labels = {
    #         'name': '菜名'
    #     }


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
