from django import forms


class NameForm(forms.ModelForm):
    your_name = forms.CharField(label='Your name', max_length=100)
