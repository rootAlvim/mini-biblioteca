from django.shortcuts import render, redirect
from .models import *
from .forms import *
import requests


def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livro.html', {'livros': livros})


def autor(request, id):
    livro = Livro.objects.filter(id=id)
    autor = Autor.objects.get(id=id)
    return render(request, 'pagina_autor.html', {'livros': autor.livros.all(), 'autor': autor})


def autores(request):
    autores = Autor.objects.all()
    return render(request, 'autores.html', {'autores': autores})


def criar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = Autor.objects.create(
                nome=form.cleaned_data['nome'],
                nacionalidade=form.cleaned_data['nacionalidade'],
            )
            return redirect('autor', id=autor.id)
    else:
        form = AutorForm()
    return render(request, 'criar_autor.html', {'form': form})


def detalhe_cidade(request):
    cidades = []
    

    resposta_cidades = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/municipios',)
    if resposta_cidades.status_code == 200:
            cidades = resposta_cidades.json()


    return render(request, 'detalhe_cidade.html', {
        'cidades_select': cidades,
    })

    