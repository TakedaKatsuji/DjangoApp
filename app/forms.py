from django import forms

class TestForm(forms.Form):
    kokugo = forms.IntegerField(label='国語')
    sannsuu = forms.IntegerField(label='算数')
    rika = forms.IntegerField(label='理科')
    syakai = forms.IntegerField(label='社会')

    