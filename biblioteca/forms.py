import re
from datetime import date

from django import forms

from .models import Autor, Categoria, Livro


class AutorForm(forms.Form):
    nome = forms.CharField(max_length=20)
    nacionalidade = forms.CharField(max_length=2, required=False)


class LivroForm(forms.ModelForm):
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano_publicacao', 'disponivel', 'categorias']
        labels = {
            'titulo': 'Título do livro',
            'autor': 'Autor',
            'ano_publicacao': 'Ano',
            'disponivel': 'Disponível',
            'categorias': 'Categorias',
        }
        widgets = {
            'disponivel': forms.CheckboxInput,
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '')
        titulo = re.sub(r'\s+', ' ', titulo.strip())

        tamanho = len(titulo)
        if tamanho < 3:
            raise forms.ValidationError(
                'O título do livro ficou muito curto após remover espaços extras. Informe pelo menos 3 caracteres, sem espaços duplicados no meio.'
            )

        return titulo

    def clean_ano_publicacao(self):
        ano = self.cleaned_data.get('ano_publicacao')
        if ano is None:
            return ano

        ano_atual = date.today().year
        if ano > ano_atual:
            raise forms.ValidationError(
                f'O ano do livro não pode ser posterior ao ano atual ({ano_atual}). Ajuste o valor para o ano atual ou anterior.'
            )

        return ano