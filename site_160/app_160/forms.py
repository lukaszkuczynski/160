from django import forms

class SummaryForm(forms.Form):
    url = forms.URLField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'url'}))
    text = forms.CharField(label='', max_length=160, widget=forms.Textarea(attrs={'placeholder': 'wpisz swój tekst...'}))
    tags = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'tagi'}))


