from django import forms

class SummaryForm(forms.Form):
    url = forms.URLField(label='link', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    text = forms.CharField(label='tekst', max_length=160, widget=forms.Textarea(attrs={'placeholder': 'to jest miejsce na twoje 160 znaków...'}))
    tags = forms.CharField(label='tagi', max_length=100, widget=forms.TextInput())


