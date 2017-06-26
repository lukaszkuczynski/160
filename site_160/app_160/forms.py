from django import forms

class SummaryForm(forms.Form):
    url = forms.CharField(label='url', max_length=100)
    summary = forms.CharField(label='summary', max_length=160)
    tags = forms.CharField(label='tags', max_length=100)


