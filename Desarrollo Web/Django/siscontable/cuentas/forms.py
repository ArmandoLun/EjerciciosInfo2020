from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Busqueda',max_length=10)
    limit = forms.IntegerField(label='Limite',min_value=1, required= False)