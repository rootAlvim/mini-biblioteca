from django import forms 

class AutorForm(forms.Form):
    nome = forms.CharField(max_length=20)
    nacionalidade = forms.CharField(max_length=2,required=False)