from django import forms

class SummaryForm(forms.Form):
    url = forms.URLField(label='link', max_length=100, widget=forms.TextInput(attrs={'placeholder':'link do oryginalego utworu'}))
    text = forms.CharField(label='tekst', max_length=160, widget=forms.Textarea(attrs={'placeholder': 'to jest miejsce na twoje 160 znaków...'}))
    tags = forms.CharField(label='tagi', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'tagi opisujące Twój wpis, przedzielone przecinkami'}))


