from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

import requests

from .forms import AutorForm, LivroForm
from .models import Autor, Livro


def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livro.html', {'livros': livros})


def autor(request, id):
    autor_obj = get_object_or_404(Autor, id=id)
    return render(request, 'pagina_autor.html', {'livros': autor_obj.livros.all(), 'autor': autor_obj})


def autores(request):
    autores = Autor.objects.all()
    return render(request, 'autores.html', {'autores': autores})


def criar_autor(request):
    if request.method == 'POST':
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


def livro_form(request, livro_id=None):
    if livro_id is not None:
        livro = get_object_or_404(Livro, id=livro_id)
        modo = 'editar'
        titulo_pagina = 'Editar livro'
        action_url = request.path
    else:
        livro = None
        modo = 'novo'
        titulo_pagina = 'Novo livro'
        action_url = '/livros/novo/'

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            livro_formulario = form.save()
            id_autor = livro_formulario.autor.id
            return redirect('autor', id=id_autor)
    else:
        form = LivroForm(instance=livro)

    return render(request, 'livro_form.html', {'form': form,'modo': modo,'titulo_pagina': titulo_pagina,'action_url': action_url,'livro': livro,})
